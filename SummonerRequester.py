from RIOTAPI import RIOTAPI, Server

class SummonerRequester:
    def __init__(self, api : RIOTAPI):
        self.api = api

    def RequestByEncryptedAccountID(self, server : Server, accountID : str):
        endpoint = "/lol/summoner/v4/summoners/by-account/{}".format(accountID)
        return self.api.request(server, endpoint)

    def RequestByName(self, server : Server, summonerName : str):
        endpoint = "/lol/summoner/v4/summoners/by-name/{}".format(summonerName)
        return self.api.request(server, endpoint)

    def RequestByEncrypedPUUID(self, server : Server, PUUID : str):
        endpoint = " /lol/summoner/v4/summoners/by-puuid/{}".format(PUUID)
        return self.api.request(server, endpoint)

    def RequestByEncrypedSummonerID(self, server : Server, summonerID : str):
        endpoint = "/lol/summoner/v4/summoners/{}".format(summonerID)
        return self.api.request(server, endpoint)