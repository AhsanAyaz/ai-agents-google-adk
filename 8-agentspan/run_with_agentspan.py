"""
AgentSpan fire-and-forget demo.

1. Start AgentSpan server first:
       agentspan server start

2. Run this script — it fires the job and exits immediately.
   The pipeline keeps running on the AgentSpan server.

3. Watch the dashboard at localhost:6767 — execution is RUNNING
   with no Python process alive.

4. Run reconnect.py with the printed execution_id to get the result.
"""

from dotenv import load_dotenv

load_dotenv()

from agentspan.agents import AgentRuntime

from agent import pipeline, TOPIC


def main():
    print(f"\nFiring research pipeline: {TOPIC}\n")

    with AgentRuntime() as runtime:
        handle = runtime.start(pipeline, TOPIC)
        print(f"Job running: {handle.execution_id}")
        print("Process exits. Job keeps running on AgentSpan server.")
        print(f"\nReconnect anytime with:")
        print(f"  python reconnect.py {handle.execution_id}")


if __name__ == "__main__":
    main()
