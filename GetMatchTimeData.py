from RIOTAPI import RIOTAPI, MajorRegion, Server
from ParsedMatchTimeLineRequester import ParsedMatchTimeLineRequester
import json
import sys

key = sys.argv[1]
quarter = int(sys.argv[2])
quarters = [(0, 3305), (3305, 6610), (6610, 9915), (9915, 13222)]


api = RIOTAPI(key)
region = MajorRegion.AMERICAS
server = Server.NA
requester = ParsedMatchTimeLineRequester(api, region, server)

with open(f"MatchIds.txt", "r") as matchFile:
    gameIds = matchFile.read().splitlines()
    if(quarter == 0):
        gameIds = gameIds[0:551]
    elif(quarter == 1):
        gameIds = gameIds[quarters[0][0]:quarters[0][1]]
    elif(quarter == 2):
        gameIds = gameIds[quarters[1][0]:quarters[1][1]]
    elif(quarter == 3):
        gameIds = gameIds[quarters[2][0]:quarters[2][1]]
    elif(quarter == 4):
        gameIds = gameIds[quarters[3][0]:quarters[3][1]]

    matches = requester.RequestMatchTimelines(gameIds)

    if(quarter == -1):
        with open(f"Matches.json", "w") as outfile:
            json.dump(matches, outfile)
    else:
        with open(f"Matches{quarter}.json", "w") as outfile:
            json.dump(matches, outfile)
