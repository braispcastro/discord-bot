import datetime
from discord.ext import commands
from Common.Configuration import Configuration
from Core.Commands.HelloWorld import HelloWorld
from Core.Commands.Twitch import Twitch
from Core.Timer import Timer

prefixes = Configuration().getDiscordPrefix()
bot = commands.Bot(command_prefix=prefixes)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# Commands
bot.add_cog(HelloWorld(bot))
bot.add_cog(Twitch(bot))


def eventChanged():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


timer = Timer(300)
timer.events.on_change += eventChanged
timer.start()

token = Configuration().getDiscordToken()
bot.run(token)
