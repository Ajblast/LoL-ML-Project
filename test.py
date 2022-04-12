import json
from RIOTAPI import RIOTAPI, MajorRegion, Server
from MatchRequester import MatchRequester
from ParsedMatchTimeLineRequester import ParsedMatchTimeLineRequester
import sys

key = sys.argv[1]

api = RIOTAPI(key)
requester = MatchRequester(api)
region = MajorRegion.AMERICAS
server = Server.NA
parser = ParsedMatchTimeLineRequester(api, region, server)

with open("MatchIds.txt", "r") as infile:
    matchID = infile.read().splitlines()[1]

    print(f":{matchID}:")

    match = requester.RequestMatch(region, matchID)
    timeline = requester.RequestMatchTimeline(region, matchID)
    parsed = parser.RequestMatchTimelines([matchID])

    with open("TestMatch.json", "w") as outfile:
        json.dump(match, outfile, indent=2)
    with open("TestTimeline.json", "w") as outfile:
        json.dump(timeline, outfile, indent=2)
    with open("TestParsed.json", "w") as outfile:
        json.dump(parsed, outfile, indent=2)