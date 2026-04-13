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
**Last generated:** 2026-04-09  
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

| Tool | Stars | Links |
|------|------|------|
| Langfuse | ⭐ ~24k+ | https://github.com/langfuse/langfuse |
| Phoenix (Arize) | ⭐ ~9k+ | https://github.com/Arize-ai/phoenix |
| Helicone | ⭐ ~5k+ | https://github.com/Helicone/helicone |
| Weave (W&B) | ⭐ ~1k+ | https://github.com/wandb/weave |
| OpenLIT | ⭐ ~2k+ | https://github.com/openlit/openlit |
| AgentOps SDK | ⭐ ~5k+ | https://github.com/AgentOps-AI/agentops |
| Opik (Comet) | ⭐ ~18k+ | https://github.com/comet-ml/opik |
| OpenLLMetry | ⭐ ~6k+ | https://github.com/traceloop/openllmetry |
| Monocle2AI | ⭐ ~70+ | https://github.com/monocle2ai/monocle |
| Dunetrace | ⭐ ~20+ | https://github.com/dunetrace/dunetrace |

Stars are approximate and evolve over time.

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=langfuse/langfuse,Arize-ai/phoenix,Helicone/helicone,wandb/weave,openlit/openlit,AgentOps-AI/agentops,comet-ml/opik,traceloop/openllmetry,monocle2ai/monocle,dunetrace/dunetrace&type=Date)](https://star-history.com/#langfuse/langfuse&Arize-ai/phoenix&Helicone/helicone&wandb/weave&openlit/openlit&AgentOps-AI/agentops&comet-ml/opik&traceloop/openllmetry&monocle2ai/monocle&dunetrace/dunetrace&Date)

---

### Paid / SaaS Tools

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

---

## Key Insights

“You do not pay for infrastructure, you pay for visibility.”

Observed patterns:

- Open source tools dominate early-stage development  
- SaaS tools dominate production and scale  
- Evaluation is becoming the primary differentiator  

---

## How to Choose

For getting started:
- Langfuse  
- Phoenix  

For evaluation-focused workflows:
- Braintrust  
- LangWatch  
- Opik  

For production environments:
- Datadog LLM  
- LangSmith  

For gateway and control:
- Helicone  

---

## Architecture Layers

The AgentOps ecosystem is converging into three main layers:

| Layer | Tools |
|------|------|
| Tracing | Langfuse, Helicone |
| Evaluation | Braintrust, Opik |
| Full Stack | LangSmith, Datadog |

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

To contribute:
1. Update data/tools.json

