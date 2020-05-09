from discord.ext import commands

from Core.DiscordEmbedHelper import DiscordEmbedHelper
from Core.TwitchManager import TwitchManager


class Twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["t", "tw"])
    async def twitch(self, ctx, *names):
        channels = TwitchManager().CheckStreams(names)
        for channel in channels:
            embed = DiscordEmbedHelper().TwitchOnline(channel)
            await ctx.send(content=None, tts=False, embed=embed)
