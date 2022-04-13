#Participants - 330 Total For all Champtions
# Chamption Stats - 25
# Total Damage Done
# Total damage to champtions
# Total damage taken
# Jungle Minions killed
# Minions killed
# Level
# Time enemy spent
# Total Gold

#Events
# Ward_placed
#   Yellow_trinket
#   blue_trinked
#   Sight_ward
#   Control_ward
# Ward_killed
#   Yellow_trinket
#   blue_trinked
#   Sight_ward
#   Control_ward

#Champion_kill
# killerId - 10 features
# victim_id - 10 features
# assistingParticipantIds (list) - 10 features

#champion_special_kill
# type: kill_ace (for team)

#building_kill
# type: tower_building - 1 feature for team
# type: INHIBITOR_BUILDING - 1 feature for team

#ELITE_MONSTER_KILL (All by team id)
# monster_type: baron_nashor
# monster_type: dragon
# monster_type: RIFTHERALD

#game_end

import json
import progressbar


with open("TestMatches.json", "r") as infile:
    matches = json.load(infile)[:1]
    
    #List of all the matches:
    widgets = ['[', progressbar.Counter(format='%(value)d/%(max_value)d'), ']', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
    for i in progressbar.progressbar(range(len(matches)), widgets=widgets):
        match = matches[i]
        #Match is a dict of [gameid, frames]


        for frame in match["frames"]:
            #Frame is a dictionary of [events, participantInfo]

            #For each event
            for event in frame["events"]:
                pass

            #All participant info for a specific frame
            participantinfo = dict()

            #For each participant
            for participantid in frame["participantInfo"]:
                #Participant is a dictionary
                participant = frame["participantInfo"][participantid]

                participantinfo[f'{participantid}_jungleMinionsKilled']         = participant['jungleMinionsKilled']
                participantinfo[f'{participantid}_level']                       = participant['level']
                participantinfo[f'{participantid}_minionsKilled']               = participant['minionsKilled']
                participantinfo[f'{participantid}_timeEnemySpentControlled']    = participant['timeEnemySpentControlled']
                participantinfo[f'{participantid}_totalGold']                   = participant['totalGold']

                #Add each stat to the dictionary of chamption stats
                for statName in participant['championStats']:
                    participantinfo[f'{participantid}_{statName}'] = participant['championStats'][statName]
