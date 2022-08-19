import discord
import asyncio
import os
from discord.ext import commands

class UhohCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uhoh(self, ctx):
        await ctx.send("uh oh")
        
async def setup(bot):
     await bot.add_cog(UhohCommand(bot))