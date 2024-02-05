from analyzeace.TaskManagement import Logger
from analyzeace import AnalyzeAce
import asyncio

environment = Logger()


async def aname():
    await AnalyzeAce().AiLoop()


def main():
    asyncio.run(aname())
