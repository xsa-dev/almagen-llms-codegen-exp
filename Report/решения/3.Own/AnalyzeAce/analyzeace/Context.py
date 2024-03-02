from pkg_resources import working_set
import os
import polars as pl


class Context:
    def __init__(self):
        self.files = None
        self.input = None
        self.output = None
        self.directory = None
        self.data = None
        self.packages = None

    def get_data(self):
        return self.data

    async def set_data(self, data=None):
        self.data = data
        self.directory = f"/Users/xsa-osx/_projects/1_projects/ALMAGEN/Interview Data"
        self.output = f"/Users/xsa-osx/_projects/1_projects/ALMAGEN/Interview Data/output.txt"

    async def enrich_context(self):
        # read all files in self.directory
        self.data = []
        self.files = await self.load_files(self.directory)
        self.packages = [(d.project_name, d.version) for d in working_set]

    async def load_files(self, directory):
        file_list = []
        for file_name in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file_name)):
                df = pl.read_csv(os.path.join(directory, file_name))
                file_list.append(
                    {
                        "file": file_name,
                        "data": df.head(n=5).to_dict(),
                    }
                )
        return file_list

    def __str__(self):
        return """
        Input Directory: {1}
        Output Directory: {2}
        Work Directory: {3}
        Files with Data: {0}        
        Environment Packages: {5}
        """.format(
            self.files,
            self.input,
            self.output,
            self.directory,
            self.data,
            self.packages
        )


class File:
    def __init__(self, path: str):
        self.path = path

    # reader
    def read_file(self):
        pass

    # writer
    def write_files(self):
        pass

    # scan dir
    def folder(self):
        pass
