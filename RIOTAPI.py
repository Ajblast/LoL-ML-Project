from enum import Enum
import requests
from RateLimit import RateLimit

class Server(Enum):
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

class MajorRegion(Enum):
    AMERICAS = "americas"
    ASIA = "asia"
    EUROPE = "europe"

class RIOTAPI:
    def __init__(self, apikey : str):
        self.key = apikey
        self.secondRateLimit = RateLimit(20, 1, 0.1, .1)
        self.minuteRateLimit = RateLimit(100, 120, 0.1, 10)


    def request(self, server : Server, endpoint : str):
        headers = {"X-Riot-Token": self.key}
        url = "https://{}.api.riotgames.com{}".format(server.value, endpoint)

        # Wait for the second rate limit
        self.secondRateLimit.waitForRateLimit()
        # Wair for the minute rate limit
        self.minuteRateLimit.waitForRateLimit()


        r = requests.get(url, headers=headers)
        return r.json()

    def requestMajorRegion(self, region : MajorRegion, endpoint : str):
        headers = {"X-Riot-Token": self.key}
        url = "https://{}.api.riotgames.com{}".format(region.value, endpoint)

        # Wait for the second rate limit
        self.secondRateLimit.waitForRateLimit()
        # Wair for the minute rate limit
        self.minuteRateLimit.waitForRateLimit()


        r = requests.get(url, headers=headers)
        return r.json()

    
