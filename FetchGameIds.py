from MatchRequester import MatchRequester
from RIOTAPI import RIOTAPI, MatchRegion

api = RIOTAPI("RGAPI-93b10d04-9914-4a44-ac94-4a183e74445c")
requester = MatchRequester(api)
region = MatchRegion.AMERICAS

with open('playerIds.txt') as playerFile:
    #Apparently readlines keeps the new line character, so it is recommended to read the entire file then split it
    allids = playerFile.read().splitlines()
    
    for i in range(0, 1):
        id = allids[i]
        retVal = requester.RequestMatchIds(region, id, 0, 10)
        print(retVal)

    #for id in allids:
        #print(":{}:".format(id))
        #requester.RequestMatchIds(id, 0, 10)