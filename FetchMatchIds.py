from RIOTAPI import RIOTAPI, MajorRegion, QueueType, Server
from LeagueRequester import LeagueRequester
from MatchRequester import MatchRequester
from SummonerRequester import SummonerRequester
import progressbar
import sys

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
    
    widgets = ['[', progressbar.Counter(format='%(value)02d/%(max_value)d'), ']','[', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
    for i in progressbar.progressbar(range(len(summonerIds)), widgets=widgets):
        id = summonerIds[i]
        summoner = summonerRequester.RequestByEncrypedSummonerID(server, id)
        summonerPUUIDs.append(summoner["puuid"])

    return summonerPUUIDs


api = RIOTAPI(sys.argv[1])
matchRequester = MatchRequester(api)
leagueRequester = LeagueRequester(api)
region = MajorRegion.AMERICAS
server = Server.NA
queueType = QueueType.Ranked5x5

print()
print("Region: {}".format(region.value))
print("Server: {}".format(server.value))
print("Queue Type: {}".format(queueType))


#Get the high elo players
leagueRequester = LeagueRequester(api)
encryptedPUUIDs = []
print("\nFetch Challenger Encrypted PUUIDS")
challengerPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestChallengerPlayers(server))
encryptedPUUIDs.extend(challengerPUUIDs)

#print("\nFetch Grandmaster Encrypted PUUIDS")
#grandmasterPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestGrandmasterPlayers(server))
#encryptedPUUIDs.extend(grandmasterPUUIDs)

#print("\nFetch Master Encrypted PUUIDS")
#masterPUUIDs = FetchEncryptedPUUIDs(api, server, leagueRequester.RequestMasterPlayers(server))
#encryptedPUUIDs.extend(masterPUUIDs)

print()
print("Total Challenger Count: {}".format(len(challengerPUUIDs)))
#print("Total Grandmaster Count: {}".format(len(grandmasterPUUIDs)))
#print("Total Master Count: {}".format(len(masterPUUIDs)))
print("Total Player Count: {}".format(len(encryptedPUUIDs)))

print("\nFetch Player Match IDs")
matchIDs = set()
widgets = ['[', progressbar.Counter(format='%(value)02d/%(max_value)d'), ']', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
for i in progressbar.progressbar(range(len(encryptedPUUIDs)), widgets=widgets):
    puuid = encryptedPUUIDs[i]
    matches = matchRequester.RequestMatchIds(region, puuid, 0, 100, queueType)
    matchIDs.update(matches)

print()
print("Total Match Count: {}".format(len(matchIDs)))

with open("MatchIds.txt", "w") as matchFile:
    for id in matchIDs:
        matchFile.write("{}\n".format(id))