import requests
import json
from RIOTAPI import RIOTAPI


api = RIOTAPI("RGAPI-93b10d04-9914-4a44-ac94-4a183e74445c")

with open('playerIds.txt') as playerFile:
    allids = playerFile.readlines()
    
    for id in allids:

#retval = api.request("/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5")
#print(type(retval))
#with open("D:\Classes\Spring 2022\Machine Learning\Project Part 2\Repo\playerIds.json", "a") as writer:
#    entries = retval["entries"]
#    playerIds = []
#    for dict in entries:
#        playerIds.append(dict["summonerId"])
#    print(len(playerIds))
#    writer.write(json.dumps(playerIds))