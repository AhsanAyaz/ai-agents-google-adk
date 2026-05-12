"""
Plain ADK run — demonstrates crash-and-restart problem.

1. Run this script and wait for the Researcher to finish.
2. Press Ctrl+C to kill the process.
3. Run again — watch Researcher start over from scratch.
"""

import asyncio

from dotenv import load_dotenv

load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import pipeline, TOPIC


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

    print(f"\nStarting research pipeline on: {TOPIC}\n")
    print("TIP: Press Ctrl+C after the Researcher finishes to see crash behaviour.\n")

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
            print("\n\n--- FINAL OUTPUT ---")
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main())
