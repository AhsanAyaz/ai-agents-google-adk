"""
Reconnect to a running or interrupted Agentspan execution.

Usage:
    python reconnect.py <execution_id>

The execution_id is printed when you first run run_with_agentspan.py.
This script can run from any process — the state lives on the Agentspan server.
"""

import sys

from dotenv import load_dotenv

load_dotenv()

from agentspan.agents import AgentHandle, AgentRuntime


def main():
    if len(sys.argv) < 2:
        log_usage()
        sys.exit(1)

    execution_id = sys.argv[1]
    log_reconnecting(execution_id)

    with AgentRuntime() as runtime:
        handle = AgentHandle(execution_id=execution_id, runtime=runtime)
        result = handle.stream().get_result()

    log_result(result)


# ---------- logging helpers (kept at bottom) ----------


def log_usage():
    print("Usage: python reconnect.py <execution_id>", flush=True)


def log_reconnecting(execution_id):
    print(f"\n[reconnect] Reconnecting to execution: {execution_id}\n", flush=True)


def log_result(result):
    print("\n--- FINAL OUTPUT ---", flush=True)
    print(result.output.get("result", result.output), flush=True)
    print(f"\n[reconnect] Status: {result.status}", flush=True)


if __name__ == "__main__":
    main()
