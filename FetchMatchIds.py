from RIOTAPI import RIOTAPI, MajorRegion, Server
from LeagueRequester import LeagueRequester
from MatchRequester import MatchRequester
from SummonerRequester import SummonerRequester

# Fetch enctyped PUUIDs from a league entry
def FetchEncryptedPUUIDs(api : RIOTAPI, server : Server, leagueEntries : dict):
    #Get their summoner names
    summonerEntries = leagueEntries["entries"]
    summonerIds = []
    for entry in summonerEntries:
        summonerIds.append(entry["summonerId"])

    #Convert the summoner Ids into encrypted puuids
    summonerRequester = SummonerRequester(api)
    summonerPUUIDs = []
    for id in summonerIds:
        summoner = summonerRequester.RequestByEncrypedSummonerID(server, id)
        summonerPUUIDs.append(summoner["puuid"])

    return summonerPUUIDs


api = RIOTAPI("RGAPI-8d6f5af5-56ca-42ce-b1b4-9f6e2b06d473")
matchRequester = MatchRequester(api)
leagueRequester = LeagueRequester(api)
region = MajorRegion.AMERICAS
server = Server.NA

#Get the high elo players
leagueRequester = LeagueRequester(api)
encryptedPUUIDs = []
encryptedPUUIDs.append(FetchEncryptedPUUIDs(api, server, leagueRequester.RequestChallengerPlayers(server)))
#encryptedPUUIDs.append(FetchEncryptedPUUIDs(api, server, leagueRequester.RequestGrandmasterPlayers(server)))
#encryptedPUUIDs.append(FetchEncryptedPUUIDs(api, server, leagueRequester.RequestMasterPlayers(server)))

# for puuid in encryptedPUUIDs:
#     match = matchRequester.RequestMatchIds(region, puuid, 0, 100)
#     print(match)

#match = matchRequester.RequestMatchIds(region, encryptedPUUIDs[0], 0, 10)
#print(match)

print(encryptedPUUIDs)

# with open('playerIds.txt') as playerFile:
#     #Apparently readlines keeps the new line character, so it is recommended to read the entire file then split it
#     allids = playerFile.read().splitlines()
    
#     for i in range(0, 1):
#         id = allids[i]
#         print(id)
#         retVal = matchRequester.RequestMatchIds(region, id, 0, 10)
#         print(retVal)

#     #for id in allids:
#         #print(":{}:".format(id))
#         #requester.RequestMatchIds(id, 0, 10)