import json
from RIOTAPI import RIOTAPI, MajorRegion
from MatchRequester import MatchRequester
import sys

key = sys.argv[1]

api = RIOTAPI(key)
requester = MatchRequester(api)
region = MajorRegion.AMERICAS

with open("MatchIds.txt", "r") as infile:
    matchID = infile.read().splitlines()[1]

    print(f":{matchID}:")

    match = requester.RequestMatch(region, matchID)
    timeline = requester.RequestMatchTimeline(region, matchID)

    with open("TestMatch.json", "w") as outfile:
        json.dump(match, outfile, indent=2)
    with open("TestTimeline.json", "w") as outfile:
        json.dump(timeline, outfile, indent=2)