import os
import asyncio
from discord.ext import commands
from sakana import *

intents.members = True
intents.presences = True
intents.message_content = True


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(intents=intents, command_prefix=prefix)
        self.command_prefix = prefix


ce = Bot()


async def load():

    await ce.load_extension("jishaku")
    await ce.load_extension("Cogs.events")
    print("🟪 initial extensions loaded")


asyncio.run(load())
ce.run(TOKEN, log_handler=None)
