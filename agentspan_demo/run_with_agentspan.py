"""
Agentspan fire-and-forget demo.

1. Start Agentspan server first:
       agentspan server start

2. Run this script — it fires the job and exits immediately.
   The pipeline keeps running on the Agentspan server.

3. Watch the dashboard at localhost:6767 — execution is RUNNING
   with no Python process alive.

4. Run reconnect.py with the printed execution_id to get the result.
"""

from dotenv import load_dotenv

load_dotenv()

from agentspan.agents import AgentRuntime

from agent import pipeline, TOPIC


def main():
    log_firing_pipeline()

    with AgentRuntime() as runtime:
        handle = runtime.start(pipeline, TOPIC)
        log_job_running(handle.execution_id)
        log_reconnect_hint(handle.execution_id)


# ---------- logging helpers (kept at bottom) ----------


def log_firing_pipeline():
    print(f"\n[run] Firing research pipeline: {TOPIC}\n", flush=True)


def log_job_running(execution_id):
    print(f"[run] Job running: {execution_id}", flush=True)
    print("[run] Process exits. Job keeps running on Agentspan server.", flush=True)


def log_reconnect_hint(execution_id):
    print("\n[run] Reconnect anytime with:", flush=True)
    print(f"  python reconnect.py {execution_id}", flush=True)


if __name__ == "__main__":
    main()
