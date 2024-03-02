import os

from crewai import Crew, Agent
from dotenv import load_dotenv

from agents import DevAgents
from data_analyst.logger import get_logger
from tasks import DevTasks

from textwrap import dedent

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
datadir = os.getenv("DATA_DIR") # TODO debug

class ResearchCrew:
    """
    This is the main class that you will use to run your custom crew.
    """

    def __init__(self, task_description, data_directory):
        self.task_description = task_description
        self.data_directory = data_directory

    def run(self):
        agents = DevAgents()
        tasks = DevTasks()

        manager: Agent = agents.senior_manager()
        architect: Agent = agents.senior_architect()
        developer: Agent = agents.senior_developer()
        agi: Agent = agents.ai_assistant()

        # Read data directory from config
        get_files_directory = tasks.get_files_from_dir(
            agent=developer,
            description="Get files from directory",
            directory=self.data_directory
        )

        # TODO FIX
        # get_data_description = tasks.get_data_description(
        #     agent=architect,
        #     description="Get data description from md files and explain to developer what scripts need to write",
        #     files=self.data_directory
        # )
        #
        # # Custom tasks include agent name and variables as input
        # get_data_frames = tasks.get_insight_from_data(
        #     agent=developer,
        #     description="Load data for csv files to DataFrames",
        #     files=get_files_directory
        # )



        # Define your custom crew here
        crew = Crew(
            agents=[manager, architect, developer, agi],
            tasks=[get_files_directory
                   # , get_data_frames, get_data_description
                   ],
            verbose=True,
        )

        return crew.kickoff()


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    logger = get_logger('research_crew')
    logger.info("## Welcome to Research DS Crew AI")
    logger.info("-------------------------------")

    research_task = dedent("""
Using the data provided, solve the following problems:
* Determine which display features are good predictors of an event (for example, an fclick event), arrange them in descending order along with a numerical assessment of their quality
* Write code for selecting, selecting parameters, training and validating a classification model in Python that predicts the probability of a click based on information about impressions
    """)
    directory_path = dedent(
        datadir.strip()
    )

    custom_crew = ResearchCrew(research_task, directory_path)

    result = custom_crew.run()

    logger.info("\n\n########################")
    logger.info("## Here is you custom crew run result:")
    logger.info("########################\n")
    logger.info(result)
