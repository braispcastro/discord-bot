from Common.Configuration import Configuration
from Core.TwitchRest import TwitchRest
from Core.DTO.TwitchData import ToUserData, ToStreamData, ToGameData, ToChannelData


class TwitchManager:

    def Authenticate(self):
        Configuration().setTwitchAccessToken(TwitchRest().Authenticate())

    def CheckStreams(self, names):
        users = TwitchRest().GetUsers(names)
        userList = self.BuildUserList(users)
        if len(userList) == 0:
            return list()
        userIds = self.BuildUserIdList(userList)
        streams = TwitchRest().GetStreams(userIds)
        streamList = self.BuildStreamList(streams)
        if len(streamList) == 0:
            return list()
        gameIds = self.BuildGameIdList(streamList)
        games = TwitchRest().GetGames(gameIds)
        gameList = self.BuildGameList(games)
        channels = self.BuildChannelList(userList, streamList, gameList)
        return channels

    def BuildUserList(self, users):
        result = list()
        for user in users:
            result.append(ToUserData(user))
        return result

    def BuildUserIdList(self, users):
        result = list()
        for user in users:
            result.append(user.id)
        return result

    def BuildStreamList(self, streams):
        result = list()
        for stream in streams:
            result.append(ToStreamData(stream))
        return result

    def BuildGameIdList(self, streams):
        result = list()
        for stream in streams:
            result.append(stream.game_id)
        return result

    def BuildGameList(self, games):
        result = list()
        for game in games:
            result.append(ToGameData(game))
        return result

    def BuildChannelList(self, users, streams, games):
        channelList = list()
        for stream in streams:
            user = next(user for user in users if user.id == stream.user_id)
            gameName = next(game.name for game in games if game.id == stream.game_id)
            isOnline = stream.type == "live"
            channel = ToChannelData(user.login, user.display_name, user.description, user.profile_image_url,
                                    gameName, stream.started_at, stream.title, isOnline, stream.viewer_count)
            channelList.append(channel)
        return channelList
