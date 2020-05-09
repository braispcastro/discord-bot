from discord.ext import commands
from Common.Configuration import Configuration
from Core.Commands.HelloWorld import HelloWorld
from Core.Commands.Twitch import Twitch

prefixes = Configuration().getDiscordPrefix()
bot = commands.Bot(command_prefix=prefixes)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Commands
bot.add_cog(HelloWorld(bot))
bot.add_cog(Twitch(bot))

token = Configuration().getDiscordToken()
bot.run(token)
