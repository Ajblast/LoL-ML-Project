from enum import Enum
import requests
from RateLimit import RateLimit

class Region(Enum):
    NA = "na1"
    BR = "br1"
    LAN = "la1"
    LAS = "la2"
    OCE = "oc1"
    KR = "kr"
    JP = "jp1"
    EUNE = "eun1"
    EUW = "euw1"
    TR = "tr1"
    RU = "ru"

class MatchRegion(Enum):
    AMERICAS = "americas"
    ASIA = "asia"
    EUROPE = "europe"

class RIOTAPI:
    def __init__(self, apikey : str):
        self.key = apikey
        self.secondRateLimit = RateLimit(20, 1, 0.1, 0.5)
        self.minuteRateLimit = RateLimit(100, 120, 0.1, 0.5)


    def request(self, region : Region, endpoint : str):
        headers = {"X-Riot-Token": self.key}
        url = "https://{}.api.riotgames.com{}".format(region, endpoint)

        # Wait for the second rate limit
        self.secondRateLimit.waitForRateLimit()
        # Wair for the minute rate limit
        self.minuteRateLimit.waitForRateLimit()


        r = requests.get(url, headers=headers)
        return r.json()

    def requestMatch(self, matchRegion : MatchRegion, endpoint : str):
        headers = {"X-Riot-Token": self.key}
        url = "https://{}.api.riotgames.com{}".format(matchRegion, endpoint)

        # Wait for the second rate limit
        self.secondRateLimit.waitForRateLimit()
        # Wair for the minute rate limit
        self.minuteRateLimit.waitForRateLimit()


        r = requests.get(url, headers=headers)
        return r.json()

    
