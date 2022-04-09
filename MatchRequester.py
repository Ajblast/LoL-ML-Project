from RIOTAPI import RIOTAPI

class MatchRequester:
    def __init__(self, api):
        self.api = api

    def RequestMatchIds(self, puuid, startIndex, count):
        if (count <= 0 or count > 100):
            raise ValueError("count must be at least 1 and less than or equal to 100")
        if (startIndex < 0):
            raise ValueError("startIndex must be at least 0")

        endpoint = "/lol/match/v5/matches/by-puuid/{}/ids?start={}&count={}".format(puuid, startIndex, count)

        return self.api.request(endpoint)
    
    def RequestMatch(self, matchid):
        endpoint = "/lol/match/v5/matches/{}".format(matchid)

        return self.api.request(endpoint)

    def RequestMatchTimeline(self, matchid):
        endpoint = "/lol/match/v5/matches/{}/timeline".format(matchid)

        return self.api.request(endpoint)