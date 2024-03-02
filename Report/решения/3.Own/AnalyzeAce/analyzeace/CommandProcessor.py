# workflow for using the LLM API
# executing plan ...
import sys


class CommandProcessor:
    def __init__(self, config, **kwargs):
        self.ui = kwargs.get("ui")
        self.config = config
        self.process = kwargs

    def enrich_context(self):
        pass

    def execute_context(self):
        pass

    def ask_plan(self):
        sys.exit('Not implemented')
        pass

    def execute_task_with_context(self):
        pass

    def validate_solved(self, attempts: int = 3):
        # TODO validate main task and save
        pass


class Util:
    def __init__(self):
        pass

    def config_utils(self):
        pass


class PandasLoader(Util):
    pass


class CodeWriter(Util):
    pass


class Vectorized(Util):
    pass


class Vcs(Util):
    pass
