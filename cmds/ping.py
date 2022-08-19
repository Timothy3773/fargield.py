import discord
import asyncio
import os
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")
        
async def setup(bot):
     await bot.add_cog(PingCommand(bot))