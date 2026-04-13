#!/usr/bin/env python3
"""
Daily README updater.
- Fetches live star counts from the GitHub API for all open-source tools.
- Rebuilds the OSS and Paid tables from data/tools.json.
- Updates the <!-- META:START/END --> block with today's date.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_JSON = os.path.join(ROOT, "data", "tools.json")
README = os.path.join(ROOT, "README.md")

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")


def github_stars(repo: str) -> tuple[int, str]:
    """Return (raw_count, formatted_label) for a GitHub repo, e.g. (24800, '24.8k')."""
    if not repo:
        return (0, "")
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        count = data.get("stargazers_count", 0)
        label = f"{count / 1000:.1f}k" if count >= 1000 else str(count)
        return (count, label)
    except Exception as exc:
        print(f"  WARN: could not fetch stars for {repo}: {exc}", file=sys.stderr)
        return (0, "?")


def build_oss_table(tools: list) -> str:
    rows = ["| Tool | Stars | Links |", "|------|------|------|"]
    oss = [t for t in tools if t.get("category") == "open_source"]

    # Fetch stars and sort descending
    enriched = []
    for t in oss:
        count, label = github_stars(t.get("github_repo", ""))
        enriched.append((count, label, t))
    enriched.sort(key=lambda x: x[0], reverse=True)

    for count, label, t in enriched:
        star_cell = f"⭐ {label}" if label and label != "?" else "⭐ ?"
        link = t.get("display_link", t.get("official_url", ""))
        rows.append(f"| {t['name']} | {star_cell} | {link} |")
    return "\n".join(rows)


def build_paid_table(tools: list) -> str:
    rows = ["| Tool | Pricing | Links |", "|------|--------|------|"]
    for t in tools:
        if t.get("category") != "paid":
            continue
        pricing = f"💰 {t['pricing_label']}" if t.get("pricing_label") else "💰 —"
        link = t.get("display_link", t.get("official_url", ""))
        rows.append(f"| {t['name']} | {pricing} | {link} |")
    return "\n".join(rows)


def replace_block(content: str, start_tag: str, end_tag: str, new_inner: str) -> str:
    pattern = re.compile(
        rf"({re.escape(start_tag)}\n).*?(\n{re.escape(end_tag)})",
        re.DOTALL,
    )
    replacement = rf"\g<1>{new_inner}\g<2>"
    result, count = pattern.subn(replacement, content)
    if count == 0:
        print(f"  WARN: marker {start_tag} not found in README", file=sys.stderr)
    return result


def main() -> None:
    with open(TOOLS_JSON, encoding="utf-8") as f:
        tools = json.load(f)

    print("Fetching star counts from GitHub API...")
    oss_table = build_oss_table(tools)
    paid_table = build_paid_table(tools)

    with open(README, encoding="utf-8") as f:
        content = f.read()

    today = date.today().isoformat()

    # Update META block
    content = replace_block(
        content,
        "<!-- META:START -->",
        "<!-- META:END -->",
        f"**Last generated:** {today}  \n**Automation:** GitHub Actions + GitHub API",
    )

    # Update OSS table
    content = replace_block(
        content,
        "<!-- OSS_TABLE:START -->",
        "<!-- OSS_TABLE:END -->",
        oss_table,
    )

    # Update Paid table
    content = replace_block(
        content,
        "<!-- PAID_TABLE:START -->",
        "<!-- PAID_TABLE:END -->",
        paid_table,
    )

    with open(README, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README updated for {today}.")


if __name__ == "__main__":
    main()
