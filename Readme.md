# Google ADK Tutorial Series: Marketing Campaign Assistant & More

This repository contains the code for a comprehensive tutorial series on **Google's Agent Development Kit (ADK)**. From building core multi-agent logic to durable execution and deployment, this project covers the full lifecycle of modern AI agents.

🎥 **Watch the Full Google ADK Tutorial Playlist:** [https://www.youtube.com/playlist?list=PL2sQdFoGnLIjoGQuK_jF92YOB-9iJAAlW](https://www.youtube.com/playlist?list=PL2sQdFoGnLIjoGQuK_jF92YOB-9iJAAlW)

---

## Project Description

This repository is organized into several modules, each representing a specific stage or feature of the Google ADK:

1.  **`marketing_campaign_agent/`**: The core multi-agent system. It automates market research, messaging, ad copy, and visual suggestions into a cohesive brief.
2.  **`tools_agent/`**: Demonstrates how to integrate custom and built-in tools (like Google Search) into your agents.
3.  **`multi_model/`**: Showcases orchestration across different models (Gemini, GPT-4, Claude) using the LiteLLM integration.
4.  **`structured_output/`**: Examples of how to enforce Pydantic schemas for reliable agent outputs.
5.  **`sessions_and_agents/`**: How to manage long-term memory and user state across multiple turns.
6.  **`deploying_agents/`**: Instructions and scripts for deploying your ADK agents to Google Cloud (Vertex AI).
7.  **`agents_and_callbacks/`**: Advanced lifecycle management using before/after hooks for logging and sanitization.
8.  **`agentspan_demo/`**: **NEW!** A deep dive into **Durable Execution**. Learn how to build agents that survive crashes and resume perfectly using Agentspan.

---

## Prerequisites

*   **Python 3.11+** (Required for Google ADK 2.0.0+)
*   **pip** (Python package installer)
*   **Google API Key** with access to Gemini models. Obtain one from [Google AI Studio](https://aistudio.google.com/).
*   Basic familiarity with Python.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AhsanAyaz/marketing-agents-adk
    cd marketing-agents-adk
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```
3.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source .venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up your API Key:**
    *   Create a file named `.env` in the project root.
    *   Add your Google API Key:
        ```env
        GOOGLE_API_KEY='YOUR_ACTUAL_GOOGLE_API_KEY'
        ```

## Project Structure

```
marketing-agents-adk/
├── marketing_campaign_agent/   # Core tutorial agent
├── tools_agent/                # Tool integration examples
├── multi_model/                # Multi-provider orchestration
├── structured_output/          # Schema enforcement
├── sessions_and_agents/        # State & Memory management
├── deploying_agents/           # Vertex AI deployment scripts
├── agents_and_callbacks/       # Lifecycle hooks
└── agentspan_demo/             # Durable execution demo
```

## How to Run the Agents

### 1. Using the ADK Web UI (`adk web`)
This is the best way to visualize the graph-based workflows:
1. Ensure your `.env` file is set up in the project root.
2. Run: `adk web .`
3. Open `http://localhost:8000` and select the agent you want to test from the dropdown.

### 2. Using the CLI (`adk run`)
Run any agent directly from your terminal:
```bash
adk run marketing_campaign_agent "Help me with a campaign for a new ergonomic chair"
```

### 3. Running the Agentspan Demo
Navigate to `agentspan_demo/` and follow the instructions in its `Readme.md` or run the `setup.sh` script to see durable execution in action.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

MIT
