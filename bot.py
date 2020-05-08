from discord.ext import commands
from Common.Configuration import Configuration
from Core.Commands.HelloWorld import HelloWorld

prefixes = Configuration().getDiscordPrefix()
bot = commands.Bot(command_prefix=prefixes)


@bot.event
async def on_ready():
    print("Logged in as {0}".format(bot.user))


# if Configuration().getIsDevMode():
bot.add_cog(HelloWorld(bot))

token = Configuration().getDiscordToken()
bot.run(token)
