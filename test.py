from RIOTAPI import RIOTAPI, MajorRegion, Server
from MatchRequester import MatchRequester

api = RIOTAPI("RGAPI-8d6f5af5-56ca-42ce-b1b4-9f6e2b06d473")
matchRequester = MatchRequester(api)
region = MajorRegion.AMERICAS
server = Server.NA

games = ["NA1_4244392212","NA1_4253050581","NA1_4254864223","NA1_4233509257","NA1_4245125532","NA1_4254430256","NA1_4221742126","NA1_4267433197","NA1_4253054644","NA1_4249438716","NA1_4240301981",
"NA1_4245172416",
"NA1_4221029907",
"NA1_4245378632",
"NA1_4196167683",
"NA1_4262104434",
"NA1_4250931024",
"NA1_4258433429",
"NA1_4253086997",
"NA1_4257833891",
"NA1_4257726072",
"NA1_4257280830",
"NA1_4241464768",
"NA1_4269106320"]

eventTypes = set()

for matchid in games:
    match = matchRequester.RequestMatchTimeline(region, matchid)

    #Frames is a list of dictionaries
    #Events is a list of dictionaries
    matchFrames = match['info']['frames']


    events = []

    #Get all of the events
    for frame in matchFrames:
        #Dictionary for each frame
        for event in frame['events']:
            eventTypes.add(event['type'])

print(eventTypes)


# Events - Champion Kill


#Cutting from info/frames/participantFrames
#   position
#   xp
#   participantId
#   goldPerSecond

#DRAGON_SOUL_GIVEN, BUILDING_KILL, CHAMION_KILL, CHAMPION_SPECIAL_KILL, WARD_PLACED, WARD_KILL, ELITE_MONSTER_KILL

#print(retval)

