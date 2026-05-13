"""
Plain ADK run — demonstrates crash-and-restart problem.

1. Run this script and wait for the Researcher to finish.
2. During the Writer countdown, press Ctrl+C to kill the process.
3. Run again — watch Researcher start over from scratch.
"""

import asyncio
import time

from dotenv import load_dotenv

load_dotenv()

from google.adk.agents.callback_context import CallbackContext
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import pipeline, writer, TOPIC


async def main():
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="research", user_id="user1", session_id="session1"
    )

    runner = Runner(
        agent=pipeline,
        app_name="research",
        session_service=session_service,
    )

    log_pipeline_start()

    events = runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text=TOPIC)],
        ),
    )

    async for event in events:
        if event.author:
            print(f"[{event.author}] ", end="", flush=True)
        if event.is_final_response():
            log_final_output(event.content.parts[0].text)


# ---------- logging hooks and helpers (kept at bottom) ----------

WRITER_DELAY_SECONDS = 2


def delay_before_writer(callback_context: CallbackContext):
    print(
        f"\n[Researcher done. Writer starts in {WRITER_DELAY_SECONDS}s — "
        "press Ctrl+C now to see crash behaviour]\n",
        flush=True,
    )
    for remaining in range(WRITER_DELAY_SECONDS, 0, -1):
        print(f"  Writer starting in {remaining}s...", flush=True)
        time.sleep(1)
    return None


def log_pipeline_start():
    print(f"\n[run] Starting research pipeline on: {TOPIC}", flush=True)
    print("[run] TIP: Press Ctrl+C during the Writer countdown to see crash behaviour.\n", flush=True)


def log_final_output(text):
    print("\n\n--- FINAL OUTPUT ---", flush=True)
    print(text, flush=True)


# Combine with agent.py's logging hooks: log first, then delay
_existing = writer.before_agent_callback
writer.before_agent_callback = (
    (_existing if isinstance(_existing, list) else [_existing] if _existing else [])
    + [delay_before_writer]
)


if __name__ == "__main__":
    asyncio.run(main())
