from RIOTAPI import RIOTAPI, MajorRegion, Server
from ParsedMatchTimeLineRequester import ParsedMatchTimeLineRequester
import json

api = RIOTAPI("RGAPI-a4adaa6a-c26c-4223-9781-aa9c82bf1ebd")
region = MajorRegion.AMERICAS
server = Server.NA
requester = ParsedMatchTimeLineRequester(api, region, server)
person = "Austin"

with open(f"MatchIds{person}.txt", "r") as matchFile:
    gameIds = matchFile.read().splitlines()

    matches = requester.RequestMatchTimelines(gameIds)

    with open(f"Matches{person}.json", "w") as outfile:
        json.dump(matches, outfile)