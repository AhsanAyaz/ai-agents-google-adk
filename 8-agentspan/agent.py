import os

from dotenv import load_dotenv

load_dotenv()

from google.adk.agents import LlmAgent, SequentialAgent

MODEL = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.5-flash")


researcher = LlmAgent(
    name="Researcher",
    model=MODEL,
    instruction="""
You are a research agent. Given a topic, produce a thorough, structured
research brief covering:
- Key facts and current state
- Notable examples or case studies
- Emerging trends and future direction

Be detailed. Your brief will be passed directly to a writer agent who will
turn it into a polished article. Write at least 500 words.
    """,
    output_key="research_brief",
)

writer = LlmAgent(
    name="Writer",
    model=MODEL,
    instruction="""
You are a technical writer. Using the research brief provided, write a
polished, well-structured article.

Include:
- An engaging introduction
- Clear sections with headers
- A concise conclusion

The research brief will be provided in the conversation context.
    """,
    output_key="final_article",
)

pipeline = SequentialAgent(
    name="ResearchPipeline",
    description="A two-stage pipeline: Researcher gathers data, Writer produces the article.",
    sub_agents=[researcher, writer],
)

root_agent = pipeline

TOPIC = "The state of durable execution for AI agents in 2026"


# ---------- logging hooks (kept at bottom to avoid cluttering agent defs) ----------


def log_before_agent(callback_context):
    print(f"[agent:start] {callback_context.agent_name}", flush=True)
    return None


def log_after_agent(callback_context):
    print(f"[agent:end]   {callback_context.agent_name}", flush=True)
    return None


researcher.before_agent_callback = log_before_agent
researcher.after_agent_callback = log_after_agent
writer.before_agent_callback = log_before_agent
writer.after_agent_callback = log_after_agent
