from RIOTAPI import RIOTAPI, MajorRegion, Server
from MatchRequester import MatchRequester
import json
import progressbar

class ParsedMatchTimeLineRequester:
    def __init__(self, api : RIOTAPI, region : MajorRegion, server : Server):
        self._matchRequester = MatchRequester(api)
        self._region = region
        self._server = server
        self._eventsCaredAbout = [ "CHAMPION_KILL", "CHAMPION_SPECIAL_KILL", "BUILDING_KILL", "ELITE_MONSTER_KILL", "DRAGON_SOUL_GIVEN", "WARD_PLACED", "WARD_KILL", "GAME_END"]

    def RequestMatchTimelines(self, gameIDs : list):
        print("\nRequest Match Timelines")

        matches = []
        widgets = ['[', progressbar.Counter(format='%(value)d/%(max_value)d'), ']', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
        for i in progressbar.progressbar(range(len(gameIDs)), widgets=widgets):
            matchid = gameIDs[i]
            match = self._matchRequester.RequestMatchTimeline(self._region, matchid)
            matchInfo = {"gameid" : matchid, "frames" : []}
            
            matchFrames = match['info']['frames']

            #Iterate over every frame
            for frame in matchFrames:        
                events = []
                #Get all of the events that we care about
                for event in frame['events']:
                    if (event['type'] in self._eventsCaredAbout):
                        events.append(event)

                #Get all of the participant information we care about
                for participantId in frame['participantFrames']:
                    del frame['participantFrames'][participantId]['goldPerSecond']
                    del frame['participantFrames'][participantId]['participantId']
                    del frame['participantFrames'][participantId]['position']
                    del frame['participantFrames'][participantId]['xp']

                frameDict = {"events": events, "participantInfo": frame['participantFrames']}
                matchInfo['frames'].append(frameDict)

            matches.append(matchInfo)

        return matches
