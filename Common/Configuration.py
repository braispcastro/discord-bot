import json


class Configuration:
    def __init__(self):
        self.isDevMode = True
        self.twitchAccessToken = None
        with open("config.json", "r") as f:
            config = json.load(f)
            self.discordClient = config["discord"]["client"]
            self.discordClientDev = config["discord"]["clientDev"]
            self.discordSecret = config["discord"]["secret"]
            self.discordSecretDev = config["discord"]["secretDev"]
            self.discordToken = config["discord"]["token"]
            self.discordTokenDev = config["discord"]["tokenDev"]
            self.discordPrefix = config["discord"]["prefix"]
            self.twitchClient = config["twitch"]["client"]
            self.twitchSecret = config["twitch"]["secret"]

    def getIsDevMode(self):
        return self.isDevMode

    def getDiscordClient(self):
        return self.discordClientDev if self.isDevMode else self.discordClient

    def getDiscordSecret(self):
        return self.discordSecretDev if self.isDevMode else self.discordSecret

    def getDiscordToken(self):
        return self.discordTokenDev if self.isDevMode else self.discordToken

    def getDiscordPrefix(self):
        return self.discordPrefix

    def getTwitchClient(self):
        return self.twitchClient

    def getTwitchSecret(self):
        return self.twitchSecret

    def getTwitchAccessToken(self):
        return self.twitchAccessToken

    def setTwitchAccessToken(self, token):
        self.twitchAccessToken = token
