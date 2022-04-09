from RIOTAPI import RIOTAPI, MajorRegion, QueueType

class MatchRequester:
    def __init__(self, api : RIOTAPI):
        self.api = api

    def RequestMatchIds(self, region : MajorRegion, puuid : str, startIndex : int, count : int, queueType : QueueType = None):
        if (count <= 0 or count > 100):
            raise ValueError("count must be at least 1 and less than or equal to 100")
        if (startIndex < 0):
            raise ValueError("startIndex must be at least 0")

        if (queueType is None):
            endpoint = "/lol/match/v5/matches/by-puuid/{}/ids?&start={}&count={}".format(puuid, startIndex, count)
        else:
            endpoint = "/lol/match/v5/matches/by-puuid/{}/ids?queue={}&start={}&count={}".format(puuid, queueType.value, startIndex, count)

        return self.api.requestMajorRegion(region, endpoint)
    
    def RequestMatch(self, region : MajorRegion, matchid : str):
        endpoint = "/lol/match/v5/matches/{}".format(matchid)

        return self.api.requestMajorRegion(region, endpoint)

    def RequestMatchTimeline(self, region : MajorRegion, matchid :str):
        endpoint = "/lol/match/v5/matches/{}/timeline".format(matchid)

        return self.api.requestMajorRegion(region, endpoint)