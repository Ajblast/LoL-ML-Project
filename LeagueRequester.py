from RIOTAPI import RIOTAPI, Server

class LeagueRequester:
    def __init__(self, api : RIOTAPI):
        self.api = api

    def RequestChallengerPlayers(self, server : Server):
        endpoint = "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(server, endpoint)

    def RequestGrandmasterPlayers(self, server : Server):
        endpoint = "/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(server, endpoint)

    def RequestMasterPlayers(self, server : Server):
        endpoint = "/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
        return self.api.request(server, endpoint)
