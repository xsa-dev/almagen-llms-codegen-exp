import os
from pathlib import Path

import openai
import yaml


class LLMInterface:

    def __init__(self):
        pass

    def config(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        return openai


class Agents:
    def __init__(self, agents=None):
        self.agents_yaml: Path = Path(agents)
        self.agents = None

    async def load_agents(self):
        with open(self.agents_yaml, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
                self.agents = data.get('agents')
            except yaml.YAMLError as exc:
                print(exc)

    async def get_agents(self):
        await self.load_agents()
        return self.agents

    async def communicate(self):
        pass
