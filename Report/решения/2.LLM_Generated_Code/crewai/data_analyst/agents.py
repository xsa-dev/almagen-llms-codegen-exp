from crewai import Agent
from textwrap import dedent

from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

from tools.data_tools import DataTool


ollama_endpoint = ""      # TODO write your own
lmstudio_endpoint = ""    # TODO write your own

class DevAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.LMStudio = ChatOpenAI(base_url=lmstudio_endpoint)
        self.Ollama = Ollama(model="openhermes:7b-v2.5", base_url=ollama_endpoint)

    def senior_architect(self):
        return Agent(
            role="Senior Architect",
            backstory=dedent("You are an Architect."),
            goal=dedent
            ("Design a concise, usable, complete python system."
             "Try to specify good open source tools as much as possible."),
            tools=[

            ],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def senior_developer(self):
        return Agent(
            role="Senior Software Engineer",
            backstory=dedent("You are a Software Engineer"),
            goal=dedent(
                """
Write elegant, readable, extensible, efficient code.
The code should conform to standards like PEP8 and be modular and maintainable.
                """),
            allow_delegation=True,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
            tools=[

            ]
        )

    def senior_manager(self):
        return Agent(
            role="Manager",
            backstory=dedent("You are а Head of the department."),
            goal=dedent(
                """
Available agents: [artificial intelligence, arhitecture specialist, software engineer specialist].
Decompose the task and choose the most suitable agents from the available agents. 
Print ONLY a list where each element is: 
<number>###<Task description>###<the most suitable agent from the available agents>
                """
            ),
            allow_delegation=True,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
            tools=[

            ]
        )

    def ai_assistant(self):
        return Agent(
            role="AI assistant",
            backstory=dedent("As an AI assistant"),
            goal=dedent(
                """
Use coding and language skills for task resolution.
Provide Python or shell scripts for data gathering. Solve the task using gathered info.
Offer complete scripts for executable tasks, clearly indicating script type.
Explain task plans, differentiating between code execution and language processing steps.
Ensure code is ready-to-run without user modifications. Include # filename: <filename> for file-saving instructions.
Use one code block per response with 'print' for outputs. Avoid requiring user edits or result copy-pasting.
Correct errors in scripts and reassess if tasks remain unsolved after successful execution.
Confirm accuracy of solutions and provide evidence when possible.
End interactions with "TERMINATE" after task completion.
                """
            ),
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=self.OpenAIGPT35,
            tools=[

            ]
        )
