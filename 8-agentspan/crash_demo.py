"""
Crash demo — fires an AgentSpan job then deliberately SIGKILL's itself.

1. Start AgentSpan server first:
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

print("Starting AgentSpan job...")

with AgentRuntime() as runtime:
    handle = runtime.start(pipeline, TOPIC)
    print(f"Execution ID: {handle.execution_id}")
    print("Job registered on AgentSpan server.")
    print("Simulating process crash in 3 seconds...")
    time.sleep(3)
    print("CRASHING NOW.")
    os.kill(os.getpid(), signal.SIGKILL)  # hard kill — no cleanup, no graceful shutdown
