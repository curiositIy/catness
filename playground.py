import asyncio

import toml
from discord.ext import commands

from sakana import *

intents.members = True
intents.presences = True
intents.message_content = True

config = toml.load("config.toml")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=prefix, intents=intents)
        self.config = config


ce = Bot()


async def load():
    await ce.load_extension("jishaku")
    await ce.load_extension("Cogs.events")
    print("🟪 initial extensions loaded")


asyncio.run(load())
ce.run(config["token"], log_handler=None)
