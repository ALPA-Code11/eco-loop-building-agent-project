# System Architecture Document: Eco-Loop Building Agent
## 1. Executive Summary
Eco-Loop is an autonomous, closed-loop building management system designed to optimize energy efficiency and thermal comfort in real time. By integrating building physics simulation (**EnergyPlus**) with Large Language Model decision-making (**Llama 3.3 70B** via **Groq**) through a standardized protocol layer (**Model Context Protocol / MCP**), Eco-Loop enables dynamic setpoint tuning without human intervention.
---
## 2. Architectural Overview
The system consists of four primary layers working synchronously in an iterative feedback loop:
```mermaid
graph TD
    Dashboard["Streamlit UI Dashboard"] <--> AgentLoop["Agentic Control Loop"]
    AgentLoop <--> GroqAPI["Groq Llama-3.3-70B API"]
    AgentLoop <--> MCPServer["Building MCP Server"]
    AgentLoop <--> SimWrapper["EnergyPlus Simulation Wrapper"]
    SimWrapper <--> EppyEngine["eppy IDF Editor"]
    EppyEngine <--> IDFFile["Base Model (.idf)"]
    SimWrapper <--> EPlusBin["EnergyPlus Binary Engine"]
    EPlusBin <--> EPWFile["Weather File (.epw)"]
