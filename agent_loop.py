import os
import json
from groq import Groq
from simulation import EnergyPlusWrapper
from mcp_server import BuildingMCPServer

# Initialize Client and MCP Server
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
mcp = BuildingMCPServer()

def run_agentic_loop():
    print("[*] Initializing Advanced Agentic MCP & Llama 3 Cognitive Engine...")

    # Initialize Simulation Wrapper
    sim_wrapper = EnergyPlusWrapper("base_model.idf", "weather_data.epw")
    sim_wrapper.run_simulation()

    # Step 1: LLM uses MCP Tool to check simulation status / errors autonomously
    print("\n[Cognitive Phase] Querying MCP Server tools for system health...")
    tool_list = mcp.list_tools()
    print(f"[*] Available MCP Tools discovered by LLM: {[t['name'] for t in tool_list]}")

    # LLM invokes error-parsing tool via protocol
    error_analysis = mcp.call_tool("parse_simulation_errors")
    print(f"[+] MCP Tool Output (Error Parser): {error_analysis}")

    # Step 2: Closed-Loop Optimization Phase with Llama 3 and MCP Live Metrics
    for step in range(1, 3):
        print(f"\n--- Agentic Optimization Step {step} ---")

        # Fetch continuous metrics via MCP Server tool call (Closed-Loop Feedback)
        live_telemetry = mcp.call_tool("get_live_metrics")

        prompt = f"""
        You are an autonomous AI Building Energy Agent connected via Model Context Protocol (MCP).
        Live Telemetry from MCP: Zone Temp = {live_telemetry['zone_temperature']}°C, Energy = {live_telemetry['energy_consumption_kwh']} kWh, PMV = {live_telemetry['pmv_thermal_comfort']}.
        System Health Check from MCP: {json.dumps(error_analysis)}

        Task: Determine the optimal cooling set-point and respond strictly in valid JSON format:
        {{
            "recommended_setpoint": <float>,
            "reasoning": "<explanation>"
        }}
        """

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a precise building automation agent utilizing MCP tools."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )

            decision = json.loads(completion.choices[0].message.content)
            print(f"[+] Llama 3 Decision: {decision.get('recommended_setpoint')}°C")
            print(f"    Reasoning: {decision.get('reasoning')}")

            # Forward injection and structural modification via eppy & simulation wrapper
            sim_wrapper.update_setpoints(decision.get('recommended_setpoint', 24.0))

            # Log remediation task via MCP tool execution
            mcp.call_tool("execute_remediation_task", {
                "action_type": "Update Cooling Setpoint",
                "details": f"Set to {decision.get('recommended_setpoint')}°C"
            })

        except Exception as e:
            print(f"[-] Agent execution error: {e}")

    print("\n[+] Advanced MCP-powered Cognitive Loop completed successfully!")

if __name__ == "__main__":
    run_agentic_loop()
