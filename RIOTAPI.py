import requests
import RateLimit

class RIOTAPI:
    def __init__(self, apikey):
        self.key = apikey
        self.secondRateLimit = RateLimit(20, 1, 0.1)
        self.minuteRateLimit = RateLimit(100, 120, 0.1)


    def request(self, endpoint):
        headers = {"X-Riot-Token": self.key}
        url = "https://na1.api.riotgames.com" + endpoint

        # Wait for the second rate limit
        self.secondRateLimit.waitForRateLimit()
        # Wair for the minute rate limit
        self.minuteRateLimit.waitForRateLimit()


        r = requests.get(url, headers=headers)
        return r.json()
