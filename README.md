# Multi-Agent AI System: Cybersecurity Incident Response (CrewAI)

## 🚨 Project Overview
This multi-agent AI system simulates a security incident response workflow using CrewAI. Agents work collaboratively, just like a real SOC team, to triage, enrich, analyze, remediate, and report an incident.

## 🧠 Agent Roles

- **Alert Triage Agent**: Filters and validates incoming alerts.
- **Threat Intelligence Agent**: Enriches incidents with IOCs from threat intelligence sources.
- **Incident Analyst Agent**: Identifies root cause and assesses impact.
- **Remediation Planner Agent**: Designs mitigation and recovery steps.
- **Incident Report Agent**: Summarizes the incident into a report.

## 🔄 Workflow
1. Raw alert received (simulated)
2. Triage Agent validates it
3. Threat Intel Agent enriches it
4. Incident Analyst evaluates damage
5. Planner provides remediation
6. Reporter generates final summary

## 🛠 Tools Used
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- LangChain
- OpenAI GPT-4

## ▶️ How to Run
```bash
pip install crewai langchain openai
python main.py
```

Ensure your OpenAI API key is set:
```bash
export OPENAI_API_KEY='your-key-here'
```

## 🎯 Outcome
An end-to-end simulated security incident report generated through agent collaboration.
