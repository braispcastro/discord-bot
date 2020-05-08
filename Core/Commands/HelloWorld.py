from discord.ext import commands


class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hi", "hola"])
    async def hello(self, ctx):
        await ctx.send("Hi, {0}!".format(ctx.author.mention))

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("ping")
