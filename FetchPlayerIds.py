from RIOTAPI import RIOTAPI, Region
from LeagueRequester import LeagueRequester
import os

api = RIOTAPI("RGAPI-93b10d04-9914-4a44-ac94-4a183e74445c")
league = LeagueRequester(api)
region = Region.NA
retval = league.challengerPlayers(region)
print(type(retval))

with open("playerIds.txt", "w") as writer:
    entries = retval["entries"]
    playerIds = []
    for dict in entries:
        playerIds.append(dict["summonerId"])
    print(len(playerIds))

    for ids in playerIds:
        writer.write("{}\n".format(ids))