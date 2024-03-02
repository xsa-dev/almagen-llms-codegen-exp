import yaml
import time
from pathlib import Path


class TaskManagement:
    def __init__(self, agents, state=None, task=None):
        self.task = None
        self.plan = None
        self.state = state
        self.agents = agents
        self.task_yaml: Path = Path(task)
        self.logger = Logger()
        self.task = None

    async def validate(self):
        try:
            return len(self.agents) > 0 and self.task is not None
        except Exception as e:
            raise Exception(f"Failed to validate the task due to: {e}")

    async def load_task(self):
        with open(self.task_yaml, 'r') as stream:
            try:
                data = yaml.safe_load(stream)
                self.task = data.get('task')
            except yaml.YAMLError as exc:
                print(exc)


class Logger:
    def __init__(self):
        self.log_stream = None

    def stream(self):
        counter = 0
        while True:
            yield f"Item <pre>{counter}</pre>"
            counter += 1
            if counter == 10:
                return

    def display(self, message):
        for i in message:
            yield i

    def bot(self, history):
        history[-1][1] = ""

        stream = self.stream()
        for character in stream:
            history[-1][1] += character
            time.sleep(0.05)
            yield history
