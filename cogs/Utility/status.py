from __future__ import annotations

import time

from typing import TYPE_CHECKING

import discord

from discord.ext import commands
from discord import app_commands

if TYPE_CHECKING:
    from playground import Bot

start_time = time.time()


class Status(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @app_commands.command(name='status', description='View info about the running instance of the bot. I \'don\'t know what i\'m saying')
    async def status(self, interaction: discord.Interaction):
        if self.bot.user is None:
            return await interaction.response.send_message("Bot is not logged in yet", ephemeral=True)

        timeUp = time.time() - start_time
        hours = timeUp / 3600
        minutes = (timeUp / 60) % 60
        seconds = timeUp % 60

        users = 0
        channel = 0
        for guild in self.bot.guilds:
            users += len(guild.members)
            channel += len(guild.channels)
        
        razy = self.bot.get_user(self.bot.owner_id or 592310159133376512) or await self.bot.fetch_user(self.bot.owner_id or 592310159133376512)

        embed = discord.Embed(title=str(self.bot.user))
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.add_field(name='Owner', value=f'`{razy.mention} ({razy.id})`', inline=True)
        embed.add_field(name='Uptime', value='`{0:.0f} hours, {1:.0f} minutes and {2:.0f} seconds`'.format(hours, minutes, seconds), inline=True)
        embed.add_field(name='Total users', value=f'`{users:,}`', inline=True)
        embed.add_field(name='Total channels', value=f'`{channel:,}`', inline=True)
        embed.add_field(name='Bot version', value='`0.6.0`', inline=True)
        embed.add_field(name='Discord.py Version', value=f'`{discord.__version__}`', inline=True)
        embed.add_field(name='Commands count', value=f'`{len(self.bot.commands):,}`', inline=True)
        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Status(bot))
