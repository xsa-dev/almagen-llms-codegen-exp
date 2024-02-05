from analyzeace.CommandProcessor import CommandProcessor
from analyzeace.Context import Context
from analyzeace.LLMInterface import LLMInterface, Agents
from analyzeace.TaskManagement import TaskManagement


class AnalyzeAce:
    def __init__(self):
        self.config = None

    async def AiLoop(self):
        root = Agents()
        task = TaskManagement(root)

        await root.load_agents()
        await task.load_task()

        context = Context()
        await context.set_data()
        await context.enrich_context()

        # TODO use LLM
        # TODO execute Plan
        workflow = CommandProcessor(self.config, task=task, root=root, context=context, ui=None)
        yield str(workflow)

        # await processor.get_plan()
        # await processor.execute_task_with_context()
        # await processor.validate_solved(attempts=3)

        # TODO input correct prompts and execute agents loops with beautiful terminal output

    def run(self):
        yield "TEST"
        # self.AiLoop()
