import urllib.parse
import requests
import json

from Common.Configuration import Configuration


class TwitchRest:

    def __init__(self):
        self.baseUrl = "https://api.twitch.tv/helix/"
        self.oauthUrl = "https://id.twitch.tv/oauth2/"

    def Authenticate(self):
        url = urllib.parse.urljoin(self.oauthUrl, "token")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": Configuration().getTwitchClient()
        }
        params = {
            "client_id": Configuration().getTwitchClient(),
            "client_secret": Configuration().getTwitchSecret(),
            "grant_type": "client_credentials"
        }

        response = requests.post(url, headers=headers, params=params)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["access_token"]

    def GetUsers(self, users):
        url = urllib.parse.urljoin(self.baseUrl, "users")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": Configuration().getTwitchClient(),
            "Authorization": f"Bearer {Configuration().getTwitchAccessToken()}"
        }
        url = url + "?"
        for user in users:
            url = url + f"login={user}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]

    def GetStreams(self, users):
        url = urllib.parse.urljoin(self.baseUrl, "streams")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": Configuration().getTwitchClient(),
            "Authorization": f"Bearer {Configuration().getTwitchAccessToken()}"
        }
        url = url + "?"
        for user in users:
            url = url + f"user_id={user}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]

    def GetGames(self, games):
        url = urllib.parse.urljoin(self.baseUrl, "games")
        headers = {
            "Content-Type": "application/json",
            "Client-ID": Configuration().getTwitchClient(),
            "Authorization": f"Bearer {Configuration().getTwitchAccessToken()}"
        }
        url = url + "?"
        for game in games:
            url = url + f"id={game}&"

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return None

        return json.loads(response.text)["data"]
