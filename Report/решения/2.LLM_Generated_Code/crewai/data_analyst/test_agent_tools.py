import unittest

from data_analyst.tools.data_tools import DataTool
from data_analyst.tools.code_tools import CodeTool
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd
from langchain_openai import OpenAI

class TestCases(unittest.TestCase):
    def test_data_tool(self):
        data = DataTool()
        data.read_directory_for_files()

        print(data.md_files)
        print(data.csv_files)
        print(data.directory)
        print(data.csv_dataframes)
        print(data.md_text)

    def test_ds_insights(self):
        data = DataTool()

        data.summary_of_data_description()
        print(data.metrics)
        print(data.problem)
        df_X = pd.read_csv(self.data.csv_files[0])
        df_Y = pd.read_csv(self.data.csv_files[1])

        agent_X = create_pandas_dataframe_agent(OpenAI(
            temperature=0
        ), [df_X, df_Y], verbose=True)



    def test_ds_clean_and_prepare(self):
        data = DataTool()

        data.clean_and_prepare_data()

    def test_code_tools(self):
        code = CodeTool()

        # TODO write code
        # TODO execute code





if __name__ == '__main__':
    unittest.main()
