from discord import Embed


class DiscordEmbedHelper:
    def TwitchOnline(self, channel):
        embed = Embed()
        embed.title = channel.displayName
        embed.description = channel.description
        embed.url = f"https://www.twitch.tv/{channel.user}"
        embed.set_thumbnail(url=channel.avatar)
        embed.add_field(name="Status", value=f":red_circle: Online ({channel.start_time})", inline=False)
        embed.add_field(name="Game", value=channel.game, inline=False)
        embed.add_field(name="Viewers", value=channel.viewer_count, inline=False)
        return embed
