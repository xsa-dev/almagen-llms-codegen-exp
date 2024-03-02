import os
import json
import pandas as pd
from enum import Enum

from crewai import Agent, Task
from langchain.tools import tool

from data_analyst.logger import get_logger

logger = get_logger(__name__)


class AIProblems(Enum):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"


class DataTool():
    def __init__(self, directory_path='data'):
        self.directory = directory_path
        self.md_files = []
        self.md_text = ""
        self.csv_files = []
        self.csv_dataframes = {}
        self.problem: AIProblems = None
        self.metrics = None

        self.X = None
        self.y = None

    @tool("Get metrics about the data in the directory")
    def load_insights_about_data_in_directory(self, directory_path='data'):
        """
        Reads a directory for files and populates lists and dictionaries with the file paths and data.

        Args:
            self: The instance of the class.

        Returns:
            None.

        Raises:
            Exception: If there is an error reading a CSV or Markdown file.

        Examples:
            # Create an instance of the class
            data_tools = DataTools()

            # Read the directory for files
            data_tools.read_directory_for_files()
        """

        self.read_directory_for_files()

    def read_directory_for_files(self):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    self.csv_files.append(file_path)
                    try:
                        self.csv_dataframes[file_path] = pd.read_csv(file_path)
                    except Exception as E:
                        logger.error(E)

                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    self.md_files.append(file_path)
                    try:
                        with open(file_path, 'r') as f:
                            self.md_text += f.read()
                    except Exception as E:
                        logger.error(E)

    def summary_of_data_description(self):
        ds = Agent(
            role='DataScience Consultant',
            goal='Correctly respond to questions about data. Answer must be short and concise.',
            backstory="You're a DataScience Consultant and you need to summarize the data from a given directory.",
            allow_delegation=False)

        task = Task(
            agent=ds,
            description=(
                'Based on the data in description, provide a summary of the AI problem that can be addressed using AI.'
                'Answer must be short and concise. Type of answer must be string: classification or regression.'
                f'{str(self.md_text)}'
            )
        )
        problem = task.execute()
        self.problem = problem

        task = Task(
            agent=ds,
            description=(
                'Based on the data in description, provide metrics to evaluate the AI problem. Answer in JSON format:'
                '[{"metric_name": "metric_value"} ...].'
                'Type of answer must be list of dictionary with keys: "metric_name" and "metric_value". Description:'
                f'{str(self.md_text)}'
            )
        )
        metrics = task.execute()
        self.metrics = json.loads(metrics)

        # TODO: На основании описания Провесди исследование библиотек машинного обучения в Python для выбора наилучшей:
        # TODO: на основании этого кода определи возможности для гипероптимизации:

    def clean_and_prepare_data(self):
        pass
