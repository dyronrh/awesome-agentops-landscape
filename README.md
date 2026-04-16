# awesome-agentops-landscape


A curated, research-driven list of the most relevant AgentOps tools in 2026, covering observability, evaluation, tracing, and cost monitoring for AI agents.

## Weekly Insight

“The future of AI is not models, it is systems of agents.”

Each week this repository highlights:
- New tools
- Real architectures
- Production lessons

---

[![GitHub stars](https://img.shields.io/github/stars/dyronrh/awesome-agentops-landscape?style=for-the-badge)](https://github.com/dyronrh/awesome-agentops-landscape)
[![License](https://img.shields.io/github/license/dyronrh/awesome-agentops-landscape?style=for-the-badge)](LICENSE)

<!-- META:START -->
**Last generated:** 2026-04-16  
**Automation:** GitHub Actions + GitHub API
<!-- META:END -->

---

## Table of Contents

- [Why AgentOps](#why-agentops)
- [What is AgentOps?](#what-is-agentops)
- [AgentOps Landscape (2026)](#agentops-landscape-2026)
  - [Open Source Tools](#open-source-tools)
  - [Star History](#star-history)
  - [Paid / SaaS Tools](#paid--saas-tools)
- [Feature Benchmark](#feature-benchmark)
- [Key Insights](#key-insights)
- [How to Choose](#how-to-choose)
- [Architecture Layers](#architecture-layers)
- [TL;DR](#tldr)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)

---

## Why AgentOps

Building AI agents is relatively easy. Operating them reliably in production is not.

Common failure points include:

- Lack of visibility into agent reasoning  
- Prompt failures without traceability  
- Uncontrolled token and infrastructure costs  
- No measurable evaluation of output quality  

AgentOps addresses these challenges by introducing operational discipline around AI agents.

---

## What is AgentOps?

**AgentOps** is the convergence of **DevOps**, **MLOps**, and **LLMOps** principles into a specialized operational discipline for autonomous LLM-powered agents. While LLMOps manages the lifecycle of individual model calls and prompt pipelines, AgentOps goes further — it governs the entire lifecycle of agents that reason, plan, invoke tools, coordinate with other agents, and evolve over time.

> *"AgentOps extends conventional DevOps/AIOps principles, introducing specialized stages, metrics, taxonomies, and architectures tailored to the stochastic and semantically rich behaviors of agentic AI systems."*  
> — Wang et al., 2025

### Core Capabilities

| Capability | Description |
|---|---|
| **Tracing** | Every agent execution is captured as a **trace** — a structured tree of **spans** representing individual units of work: LLM calls, tool invocations, retrieval steps, reasoning chains, and inter-agent messages. Built on **OpenTelemetry** (`gen_ai.*` semantic conventions), traces make the full decision path visible and reproducible. |
| **Monitoring** | Real-time tracking of latency, token cost, error rates, tool success rates, and session-level statistics across single and multi-agent deployments. |
| **Evaluation** | Multi-dimensional assessment of agent behavior: (1) **Final response** quality, (2) **Step-level** evaluation of individual tool selections, and (3) **Trajectory evaluation** — whether the agent followed the expected sequence of actions to reach the goal. |
| **Agent-as-Judge (LLM-as-Judge)** | An LLM is used as an automated evaluator to score agent outputs and trajectories against defined rubrics — covering correctness, tool usage accuracy, planning quality, parameter extraction, and reflection — scaling evaluation without constant human annotation. |
| **Prompt Management** | Versioning, A/B testing, and security scanning (injection detection, secret leak prevention) of prompts across agent configurations. |
| **Feedback Loops** | Collection of explicit (ratings, thumbs up/down) and implicit (click-through, acceptance rates) feedback, attached to execution traces to drive continuous improvement and fine-tuning. |
| **Guardrails & Governance** | Predefined safety constraints, fallback paths, and escalation rules that limit unsafe tool usage and keep agents aligned with business goals and compliance requirements. |

### Why AgentOps is Different from LLMOps

| Dimension | LLMOps | AgentOps |
|---|---|---|
| **Scope** | Single LLM calls, prompt pipelines | Multi-step reasoning, tool chains, agent-to-agent workflows |
| **Execution** | Stateless, short-lived | Stateful, long-running, self-evolving |
| **Evaluation unit** | Input/output quality | Final response + step correctness + trajectory |
| **Observability** | Token counts, latency | Traces, spans, reasoning graphs, memory state |
| **Accountability** | Model provider | Shared: agent owner, FM provider, tool providers |

### Technical Foundation

AgentOps platforms are instrumented via **OpenTelemetry**, where each agent session produces a **trace** composed of nested **spans** — one per LLM call, tool invocation, retrieval operation, or reasoning step. These spans capture token usage, latency, inputs/outputs, and evaluation scores, and are exported to backends like Jaeger, Langfuse, or LangSmith. **Agent-as-Judge** evaluators run asynchronously over these traces to automatically assess trajectory accuracy and output quality at scale.

### Key Challenges AgentOps Addresses

- **Non-determinism**: same input → different outputs across runs
- **Autonomy risk**: unintended tool selection or unsafe actions
- **Complex pipelines**: multi-agent orchestration with shared accountability
- **Continuous evolution**: agents that self-adapt through feedback and fine-tuning
- **Cost visibility**: token-level spend tracking across long multi-step sessions

---

> *Primary reference: Dong, Lu & Zhu — ["AgentOps: Enabling Observability of LLM Agents"](https://arxiv.org/abs/2411.05285) (CSIRO, 2024)*  
> *Also informed by: MLflow LLMOps docs, Arize AI agent observability, OpenTelemetry GenAI SIG semantic conventions, Wang et al. (2025), and industry practice as of 2026.*

---

## AgentOps Landscape (2026)

### Open Source Tools

<!-- OSS_TABLE:START -->
| Tool | Stars | Links |
|------|------|------|
| LiteLLM | ⭐ 43.5k | https://github.com/BerriAI/litellm |
| Langfuse | ⭐ 25.0k | https://github.com/langfuse/langfuse |
| Promptfoo | ⭐ 20.1k | https://github.com/promptfoo/promptfoo |
| Opik (Comet) | ⭐ 18.9k | https://github.com/comet-ml/opik |
| AgentNeo | ⭐ 16.1k | https://github.com/raga-ai-hub/RagaAI-Catalyst |
| DeepEval | ⭐ 14.8k | https://github.com/confident-ai/deepeval |
| RAGAS | ⭐ 13.4k | https://github.com/explodinggradients/ragas |
| Phoenix (Arize) | ⭐ 9.3k | https://github.com/Arize-ai/phoenix |
| Evidently AI | ⭐ 7.4k | https://github.com/evidentlyai/evidently |
| OpenLLMetry | ⭐ 7.0k | https://github.com/traceloop/openllmetry |
| Guardrails AI | ⭐ 6.7k | https://github.com/guardrails-ai/guardrails |
| Helicone | ⭐ 5.5k | https://github.com/Helicone/helicone |
| AgentOps SDK | ⭐ 5.5k | https://github.com/AgentOps-AI/agentops |
| Agenta | ⭐ 4.0k | https://github.com/agenta-ai/agenta |
| Laminar | ⭐ 2.8k | https://github.com/lmnr-ai/lmnr |
| OpenLIT | ⭐ 2.4k | https://github.com/openlit/openlit |
| Weave (W&B) | ⭐ 1.1k | https://github.com/wandb/weave |
| Monocle2AI | ⭐ 75 | https://github.com/monocle2ai/monocle |
| Dunetrace | ⭐ 25 | https://github.com/dunetrace/dunetrace |
<!-- OSS_TABLE:END -->

Stars updated daily via GitHub Actions.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=langfuse/langfuse,Arize-ai/phoenix,Helicone/helicone,wandb/weave,openlit/openlit,AgentOps-AI/agentops,comet-ml/opik,traceloop/openllmetry,monocle2ai/monocle,dunetrace/dunetrace,BerriAI/litellm,confident-ai/deepeval,explodinggradients/ragas,promptfoo/promptfoo,evidentlyai/evidently,guardrails-ai/guardrails&type=Date)](https://star-history.com/#langfuse/langfuse&Arize-ai/phoenix&Helicone/helicone&wandb/weave&openlit/openlit&AgentOps-AI/agentops&comet-ml/opik&traceloop/openllmetry&monocle2ai/monocle&dunetrace/dunetrace&BerriAI/litellm&confident-ai/deepeval&explodinggradients/ragas&promptfoo/promptfoo&evidentlyai/evidently&guardrails-ai/guardrails&Date)

---

### Paid / SaaS Tools

<!-- PAID_TABLE:START -->
| Tool | Pricing | Links |
|------|--------|------|
| LangSmith | 💰 ~$39/mo | https://smith.langchain.com |
| LangWatch | 💰 €59+ | https://langwatch.ai |
| Braintrust | 💰 ~$249/mo | https://www.braintrustdata.com |
| Datadog LLM | 💰 ~$8 / 10K req | https://www.datadoghq.com |
| Helicone Cloud | 💰 ~$79+ | https://www.helicone.ai |
| Confident AI | 💰 ~$19.99 | https://www.confident-ai.com |
| HoneyHive | 💰 Custom | https://www.honeyhive.ai |
| Langfuse Cloud | 💰 ~$29 | https://langfuse.com |
| Latitude | 💰 Free trial + usage-based | https://latitude.so |
| Maxim AI | 💰 Custom | https://www.getmaxim.ai |
| Galileo | 💰 From $5K/mo (enterprise) | https://www.rungalileo.io |
| Okahu Cloud | 💰 Custom | https://www.okahu.ai |
| Fiddler AI | 💰 Custom | https://www.fiddler.ai |
| Patronus AI | 💰 Custom | https://www.patronus.ai |
| Coval | 💰 Custom | https://www.coval.dev |
| Vellum | 💰 Free (Pro: $25/mo) | https://www.vellum.ai |
| RagaAI Catalyst | 💰 Custom | https://raga.ai |
| Portkey | 💰 Free tier + usage-based | https://portkey.ai |
<!-- PAID_TABLE:END -->

---

## Feature Benchmark

Coverage of the 8 core AgentOps capabilities per tool.

| Column | Description |
|--------|-------------|
| **Tracing** | Captures spans/traces of agent execution (LLM calls, tool invocations, reasoning steps) |
| **Monitoring** | Real-time dashboards — latency, error rates, token usage, session metrics |
| **Evaluation** | Automated quality scoring of agent outputs and trajectories (LLM-as-Judge, metrics) |
| **Prompt Mgmt** | Prompt versioning, A/B testing, injection detection |
| **Cost Tracking** | Token-level spend tracking across providers and sessions |
| **Guardrails** | Input/output validation and safety constraints at runtime |
| **Feedback** | Collection of explicit/implicit user feedback attached to traces |
| **Multi-agent** | Native support for tracing/evaluating multi-agent orchestration |

### Open Source

| Tool | Tracing | Monitoring | Evaluation | Prompt Mgmt | Cost Tracking | Guardrails | Feedback | Multi-agent |
|------|:-------:|:----------:|:----------:|:-----------:|:-------------:|:----------:|:--------:|:-----------:|
| LiteLLM | | ✅ | | | ✅ | | | ✅ |
| Langfuse | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| Promptfoo | | | ✅ | ✅ | | ✅ | | |
| Opik (Comet) | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| AgentNeo | ✅ | ✅ | ✅ | | ✅ | | | ✅ |
| DeepEval | | | ✅ | | | | | |
| RAGAS | | | ✅ | | | | | |
| Phoenix (Arize) | ✅ | ✅ | ✅ | | ✅ | | ✅ | ✅ |
| Evidently AI | | ✅ | ✅ | | | | | |
| OpenLLMetry | ✅ | ✅ | | | ✅ | | | ✅ |
| Guardrails AI | | | | | | ✅ | | |
| Helicone | ✅ | ✅ | | | ✅ | | | |
| AgentOps SDK | ✅ | ✅ | | | ✅ | | ✅ | ✅ |
| Agenta | | | ✅ | ✅ | | | ✅ | |
| Laminar | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| OpenLIT | ✅ | ✅ | | | ✅ | | | ✅ |
| Weave (W&B) | ✅ | ✅ | ✅ | | ✅ | | ✅ | ✅ |
| Monocle2AI | ✅ | ✅ | | | | | | ✅ |
| Dunetrace | ✅ | ✅ | | | | | | ✅ |

### Paid / SaaS

| Tool | Tracing | Monitoring | Evaluation | Prompt Mgmt | Cost Tracking | Guardrails | Feedback | Multi-agent |
|------|:-------:|:----------:|:----------:|:-----------:|:-------------:|:----------:|:--------:|:-----------:|
| LangSmith | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| LangWatch | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Braintrust | ✅ | | ✅ | ✅ | ✅ | | ✅ | ✅ |
| Datadog LLM | ✅ | ✅ | | | ✅ | | | ✅ |
| Helicone Cloud | ✅ | ✅ | | | ✅ | | | |
| Confident AI | | | ✅ | | | | | |
| HoneyHive | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| Langfuse Cloud | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| Latitude | ✅ | ✅ | ✅ | ✅ | ✅ | | ✅ | ✅ |
| Maxim AI | ✅ | ✅ | ✅ | ✅ | | | ✅ | ✅ |
| Galileo | ✅ | ✅ | ✅ | | | ✅ | | ✅ |
| Okahu Cloud | ✅ | ✅ | | | | | | ✅ |
| Fiddler AI | ✅ | ✅ | ✅ | | | ✅ | | ✅ |
| Patronus AI | | | ✅ | | | ✅ | | |
| Coval | | | ✅ | | | | | ✅ |
| Vellum | ✅ | ✅ | ✅ | ✅ | | | | ✅ |
| RagaAI Catalyst | ✅ | ✅ | ✅ | | ✅ | | ✅ | ✅ |
| Portkey | ✅ | ✅ | | | ✅ | ✅ | | ✅ |

---

## Key Insights

“You do not pay for infrastructure, you pay for visibility.”

Observed patterns:

- Open source tools dominate early-stage development  
- SaaS tools dominate production and scale  
- Evaluation is becoming the primary differentiator  

---

## How to Choose

**Getting started (OSS, free):**
- Langfuse — tracing + analytics out of the box
- Phoenix — debugging & evaluation with a local UI
- AgentOps SDK — drop-in agent tracking with minimal setup

**Evaluation-focused:**
- DeepEval / RAGAS — open source, 50+ metrics, great for CI pipelines
- Braintrust / LangWatch — managed, strong eval workflow tooling
- Opik — evaluation + tracing in one OSS package
- Promptfoo — red teaming & regression testing via CLI

**Production & enterprise:**
- LangSmith — full-stack tracing & evaluation for LangChain-heavy teams
- Datadog LLM — enterprise-grade, existing Datadog customers
- Galileo — hallucination detection + real-time guardrails
- Fiddler AI — AI governance and compliance at scale

**Gateway, routing & cost control:**
- LiteLLM — unified OSS gateway, 100+ providers, cost tracking
- Helicone — OSS proxy with caching and analytics
- Portkey — multi-provider routing + guardrails + observability

**Guardrails & safety:**
- Guardrails AI — OSS input/output validation framework
- Galileo — real-time production guardrails
- Patronus AI — automated hallucination detection

**ML monitoring & drift:**
- Evidently AI — OSS data/model drift detection
- Weave (W&B) — ML experiment tracking extended to LLMs

---

## Architecture Layers

The AgentOps ecosystem spans five layers:

| Layer | Purpose | Tools |
|------|---------|------|
| **Gateway & Routing** | Proxy, cost control, multi-provider | LiteLLM, Helicone, Portkey |
| **Tracing & Observability** | Spans, traces, session replay | Langfuse, Phoenix, OpenLIT, OpenLLMetry, Laminar, AgentOps SDK, Monocle2AI |
| **Evaluation** | Quality scoring, regression, red-teaming | DeepEval, RAGAS, Promptfoo, Opik, Braintrust, Agenta |
| **Guardrails & Safety** | Input/output validation, hallucination detection | Guardrails AI, Galileo, Patronus AI |
| **Monitoring & Drift** | Model drift, cost tracking, data quality | Evidently AI, Weave (W&B), Datadog LLM |

---

## TL;DR

- Open source tools provide flexibility and lower cost  
- SaaS tools provide scalability and operational maturity  
- Evaluation capabilities are the main competitive advantage  

---

## Disclaimer

This repository is a curated list based on research as of 2026.  
Pricing, features, and adoption metrics may change over time.

---

## Support

If this repository is useful:

- Star it  
- Share it  
- Follow for updates on AgentOps and AI systems  

---

## Contributing

Pull requests are welcome.

### Adding a tool

The README tables are generated automatically every day from [data/tools.json](data/tools.json).  
To add a new tool, open a PR that appends an entry to that file — the pipeline will pick it up and update the lists on the next scheduled run.

**Required fields:**

```json
{
  "name": "Tool Name",
  "category": "open_source",
  "focus": "One-line description of what it does",
  "official_url": "https://...",
  "github_repo": "owner/repo",
  "docs_url": "https://...",
  "pricing_label": "",
  "pricing_url": "",
  "display_link": "https://github.com/owner/repo"
}
```

- Set `"category"` to `"open_source"` or `"paid"`.
- For paid tools, fill `"pricing_label"` (e.g. `"~$49/mo"`) and `"pricing_url"`.
- For open-source tools, leave `"pricing_label"` empty — star counts are fetched live from `"github_repo"`.
- Open-source tools are sorted automatically by star count; no need to worry about order.

