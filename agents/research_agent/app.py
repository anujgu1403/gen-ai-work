from google.adk.apps import App
from .agent import root_agent

app = App(
    name="research_agent_app",
    root_agent=root_agent,
)