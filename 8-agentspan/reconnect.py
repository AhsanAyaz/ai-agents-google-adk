"""
Reconnect to a running or interrupted AgentSpan execution.

Usage:
    python reconnect.py <execution_id>

The execution_id is printed when you first run run_with_agentspan.py.
This script can run from any process — the state lives on the AgentSpan server.
"""

import sys

from dotenv import load_dotenv

load_dotenv()

from agentspan.agents import AgentHandle, AgentRuntime


def main():
    if len(sys.argv) < 2:
        print("Usage: python reconnect.py <execution_id>")
        sys.exit(1)

    execution_id = sys.argv[1]
    print(f"\nReconnecting to execution: {execution_id}\n")

    with AgentRuntime() as runtime:
        handle = AgentHandle(execution_id=execution_id, runtime=runtime)
        result = handle.stream().get_result()

    print("\n--- FINAL OUTPUT ---")
    print(result.output.get("result", result.output))
    print(f"\nStatus: {result.status}")


if __name__ == "__main__":
    main()
