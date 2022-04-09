from RIOTAPI import RIOTAPI, MajorRegion, QueueType, Server
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
queueType = QueueType.Ranked5x5

#Get the high elo players
leagueRequester = LeagueRequester(api)
encryptedPUUIDs = []
challengerPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestChallengerPlayers(server))
grandmasterPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestGrandmasterPlayers(server))
masterPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestMasterPlayers(server))
encryptedPUUIDs.append(challengerPUUIDs)
encryptedPUUIDs.append(grandmasterPUUIDs)
encryptedPUUIDs.append(masterPUUIDs)


print("Region: {}".format(region.value))
print("Server: {}".format(server.value))
print("Queue Type: {}".format(queueType))
print()
print("Total Challenger Count: {}".format(len(challengerPUUIDs)))
print("Total Grandmaster Count: {}".format(len(grandmasterPUUIDs)))
print("Total Master Count: {}".format(len(masterPUUIDs)))
print("Total Player Count: {}".format(len(encryptedPUUIDs)))

matchIDs = set()
for puuid in encryptedPUUIDs:
    matches = matchRequester.RequestMatchIds(region, puuid, 0, 100, queueType)
    matchIDs.update(matches)

print()
print("Total Match Count: {}".format(len(matchIDs)))

with open("MatchIds.txt", "w") as matchFile:
    for id in matchIDs:
        matchFile.write("{}\n".format(id))