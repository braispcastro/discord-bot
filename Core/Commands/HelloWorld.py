from discord.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hi", "hola"])
    async def hello(self, ctx):
        await ctx.send(f"Hi, {ctx.author.mention}!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("ping")

