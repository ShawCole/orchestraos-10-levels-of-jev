# ⚡ 10 Levels of Jev for OrchestraOS

> **A high-speed, sub-300ms structured decision engine and autonomous fleet optimization architecture.**  
> Adapted specifically from Daniel Disler's (*disler/ten-levels-of-jev*) framework for the **OrchestraOS** multi-agent operating system.

[![Live Deliverable](https://img.shields.io/badge/Live_Deliverable-Netlify-00C7B7?style=for-the-badge&logo=netlify)](https://orchestraos-10-levels-of-jev.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Fleet_Operations ["🛸 OrchestraOS Fleet Core"]
        Rotation["Blue/Green Agent Rotation (bg_beat.py)"]
        Consensus["Multi-Model Congruence (consensus.py)"]
        Gateway["Watch & Quest Gateway (watch_gateway.py)"]
        Lineage["WAL & Lineage Daemon (lineage_daemon.py)"]
    end

    subgraph Jev_Decision_Engine ["⚡ Sub-300ms System-1 Decision Layer"]
        L1["L1: Precondition Gates"]
        L2["L2: Message Intent Triage"]
        L3["L3: Rotation Risk Scoring"]
        L4["L4: Confidence Gating"]
        L5["L5: Model Runtime Router"]
        L6["L6: Tmux Syntax Guardrails"]
        L7["L7: Lineage Compaction"]
        L8["L8: Cheap Repo Scouting"]
        L9["L9: Fleet-Scale Auditing"]
        L10["L10: Consensus Self-Healing"]
    end

    Fleet_Operations <--> Jev_Decision_Engine
```

---

## 🚀 The 10 Levels Mapped to OrchestraOS

| Level | Name | OrchestraOS Integration | Core Defect / Failure Mode Solved |
|---|---|---|---|
| **L1** | **Fast Boolean Gate** | `bg_beat.py` & `precondition_gate()` | Replaces 5-second LLM reasoning with a ~250ms check on PID presence and drained WAL deltas. |
| **L2** | **Multiple Choice Triage** | `msg_store.py` & `watch_gateway.py` | Categorizes incoming fleet messages (`P0_OUTAGE`, `CONGRUENCE_VOTE`, `QUESTIONNAIRE`) in real-time. |
| **L3** | **Composite Risk Scoring** | `rotation_autonomy.py` | Computes multi-factor risk (context saturation %, git uncommitted diff churn, idle time) to prevent context blowout. |
| **L4** | **Confidence Threshold Gate** | `execute_tmux_repin()` | Gating destructive actions: $>0.92$ auto-executes; $<0.92$ routes to human approval card on Watch/Quest. |
| **L5** | **Multi-Runtime Routing** | `agent_dispatcher.py` | Cost/speed router: lightweight tasks to Gemini 2.5 Flash / Local MLX, heavy refactoring to Claude 3.7 Opus. |
| **L6** | **Invisible Guardrail Hook** | `agent_runtime.py` `pre_tool_hook()` | Intercepts raw shell commands and rewrites bare tmux targets (`-t P-g1`) into exact targets (`-t =P-g1`). |
| **L7** | **Context Compaction Hook** | `lineage_daemon.py` | Turn-end hook checking token density; compresses past conversation history to WAL before context limits. |
| **L8** | **Cheap Reads** | `repo_scout.py` | Evaluates missing helper signatures across 50+ repo files without loading raw files into the LLM context. |
| **L9** | **Fleet-Scale Scouting** | `fleet_audit.py` | Concurrent background audit of all 14 active seats for drift, zombie husks, and dead sockets. |
| **L10** | **Agentic Self-Healing** | `consensus_autodrive.py` | Detects consensus deadlocks caused by dead voter seats, auto-synthesizes fallback quorum, and unblocks pipeline. |

---

## 🛠️ Quickstart & Verification

```bash
# Clone the repository
git clone https://github.com/ShawCole/orchestraos-10-levels-of-jev.git
cd orchestraos-10-levels-of-jev

# Install dependencies
pip install -r requirements.txt

# Run the 10-level automated verification suite
python -m pytest tests/test_10_levels.py -v

# Run the live benchmark evaluator
python src/orchestra_jev_evaluator.py --level 3 --simulate
```

---

## 👥 Authors & Collaborators
- **Target Architecture:** OrchestraOS Fleet System (VPS `srv1397016`)
- **Key Collaborators:** Shaw Cole & Viorel
- **Inspiration:** Daniel Disler (`disler/ten-levels-of-jev`) & TypeSafe System-1
