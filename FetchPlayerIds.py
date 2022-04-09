from RIOTAPI import RIOTAPI
import os

api = RIOTAPI("RGAPI-93b10d04-9914-4a44-ac94-4a183e74445c")
retval = api.request("/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5")
print(type(retval))

with open("playerIds.txt", "w") as writer:
    entries = retval["entries"]
    playerIds = []
    for dict in entries:
        playerIds.append(dict["summonerId"])
    print(len(playerIds))

    for ids in playerIds:
        writer.write(ids + "\n")