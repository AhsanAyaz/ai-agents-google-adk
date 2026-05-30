"""
Crash demo — fires an Agentspan job then deliberately SIGKILL's itself.

1. Start Agentspan server first:
       agentspan server start

2. Run this script — it registers the job, prints the execution ID,
   waits 3 seconds, then hard-crashes with SIGKILL.

3. Watch localhost:6767 — execution stays RUNNING with no process alive.

4. Reconnect from any terminal to get the result:
       python reconnect.py <execution_id>
"""

import os
import signal
import time

from dotenv import load_dotenv

load_dotenv()

from agentspan.agents import AgentRuntime

from agent import pipeline, TOPIC

def main():
    log_job_starting()

    with AgentRuntime() as runtime:
        handle = runtime.start(pipeline, TOPIC)
        log_execution_id(handle.execution_id)
        log_job_registered()
        log_crash_countdown(2)
        time.sleep(2)
        log_crashing()
        os.kill(os.getpid(), signal.SIGKILL)  # hard kill — no cleanup, no graceful shutdown


# ---------- logging helpers (kept at bottom) ----------


def log_job_starting():
    print("[crash_demo] Starting Agentspan job...", flush=True)


def log_execution_id(execution_id):
    print(f"[crash_demo] Execution ID: {execution_id}", flush=True)


def log_job_registered():
    print("[crash_demo] Job registered on Agentspan server.", flush=True)


def log_crash_countdown(seconds):
    print(f"[crash_demo] Simulating process crash in {seconds} seconds...", flush=True)


def log_crashing():
    print("[crash_demo] CRASHING NOW.", flush=True)


if __name__ == "__main__":
    main()
