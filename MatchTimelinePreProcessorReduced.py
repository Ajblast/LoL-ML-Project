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

validWardTypes = ['YELLOW_TRINKET', "BLUE_TRINKET", "SIGHT_WARD", "CONTROL_WARD"]
team100Ids = [1, 2, 3, 4, 5]
team200Ids = [6, 7, 8, 9, 10]

mactchdict = dict()

with open("Matches2-3.json", "r") as infile:
    matches = json.load(infile)   

    #List of all the matches:
    widgets = ['[', progressbar.Counter(format='%(value)d/%(max_value)d'), ']', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
    for i in progressbar.progressbar(range(len(matches)), widgets=widgets):
        if(i >= 1):
            break
        print("loop" + str(i))
        match = matches[i]
        #Match is a dict of [gameid, frames]

        overalldict = dict()

        matchinfo = dict()
        teaminfo = dict()

        teaminfo['Team100_Aces'] = 0
        teaminfo['Team200_Aces'] = 0
        teaminfo['Team100_TowerKills'] = 0
        teaminfo['Team200_TowerKills'] = 0
        teaminfo['Team100_InhibKills'] = 0
        teaminfo['Team200_InhibKills'] = 0
        teaminfo['Team100_Barons'] = 0
        teaminfo['Team200_Barons'] = 0
        teaminfo['Team100_RiftHeralds'] = 0
        teaminfo['Team200_RiftHeralds'] = 0
        teaminfo['Team100_Dragons'] = 0
        teaminfo['Team200_Dragons'] = 0

        #All participant info for a specific frame
        participantinfo = dict()
        for i in range(1, 11):
            #participantinfo[f'Champ{i}_wardsPlaced'] = 0
            #participantinfo[f'Champ{i}_wardsKilled'] = 0
            participantinfo[f'Champ{i}_kills'] = 0
            participantinfo[f'Champ{i}_deaths'] = 0
            #participantinfo[f'Champ{i}_assists'] = 0

        frameid = 0
        for frame in match["frames"]:
            #Frame is a dictionary of [events, participantInfo]

            #For each event
            for event in frame["events"]:
                eventType = event['type']

                if (eventType == 'WARD_PLACED') and (event['wardType'] in validWardTypes):
                    #id = event["creatorId"]
                    #participantinfo[f'Champ{id}_wardsPlaced'] += 1
                    continue
                elif (eventType == 'WARD_KILL') and (event['wardType'] in validWardTypes):
                    #id = event["killerId"]
                    #if(id != 0):
                    #    participantinfo[f'Champ{id}_wardsKilled'] += 1
                    continue
                elif (eventType == 'CHAMPION_KILL'):
                    killerId = event['killerId']
                    victimId = event['victimId']

                    if (killerId != 0):
                        participantinfo[f'Champ{killerId}_kills'] += 1
                    participantinfo[f'Champ{victimId}_deaths'] += 1

                    if "assistingParticipantIds" in event.keys():
                        for assitId in event['assistingParticipantIds']:
                            #participantinfo[f'Champ{assitId}_assists'] += 1
                            continue
                elif (eventType == 'CHAMPION_SPECIAL_KILL') and event['killType'] == "KILL_ACE":
                    if (event['killerId'] in team100Ids):
                        teaminfo['Team100_Aces'] += 1
                    elif (event['killerId'] in team200Ids):
                        teaminfo['Team200_Aces'] += 1
                elif (eventType == 'BUILDING_KILL'):
                    if (event['buildingType'] == "TOWER_BUILDING"):
                        if (event['killerId'] in team100Ids):
                            teaminfo[f'Team100_TowerKills'] += 1
                        elif (event['killerId'] in team200Ids):
                            teaminfo[f'Team200_TowerKills'] += 1
                    elif (event['buildingType'] == "INHIBITOR_BUILDING"):
                        if (event['killerId'] in team100Ids):
                            teaminfo[f'Team100_InhibKills'] += 1
                        elif (event['killerId'] in team200Ids):
                            teaminfo[f'Team200_InhibKills'] += 1
                    pass
                elif (eventType == 'ELITE_MONSTER_KILL'):
                    teamid = event['killerTeamId']
                    if(event['monsterType'] == 'RIFTHERALD'):
                        if (event['killerId'] in team100Ids):
                            teaminfo['Team100_RiftHeralds'] += 1
                        elif (event['killerId'] in team200Ids):
                            teaminfo['Team200_RiftHeralds'] += 1
                    if(event['monsterType'] == 'DRAGON'):
                        teaminfo[f'Team{teamid}_Dragons'] += 1
                    if(event['monsterType'] == 'BARON_NASHOR'):
                        teaminfo[f'Team{teamid}_Barons'] += 1
                    pass
                elif (eventType == 'GAME_END'):
                    matchinfo['WinningTeam'] = event['winningTeam']

            #For each participant
            for participantid in frame["participantInfo"]:
                #Participant is a dictionary
                participant = frame["participantInfo"][participantid]

                #Base damage
                participantinfo[f'Champ{participantid}_jungleMinionsKilled']         = participant['jungleMinionsKilled']
                participantinfo[f'Champ{participantid}_level']                       = participant['level']
                participantinfo[f'Champ{participantid}_minionsKilled']               = participant['minionsKilled']
                #participantinfo[f'Champ{participantid}_timeEnemySpentControlled']    = participant['timeEnemySpentControlled']
                participantinfo[f'Champ{participantid}_totalGold']                   = participant['totalGold']

                #Damage stats
                participantinfo[f'Champ{participantid}_totalDamageDone']             = participant['damageStats']['totalDamageDone']
                participantinfo[f'Champ{participantid}_totalDamageDoneToChampions']  = participant['damageStats']['totalDamageDoneToChampions']
                participantinfo[f'Champ{participantid}_totalDamageTaken']            = participant['damageStats']['totalDamageTaken']

                #Add each stat to the dictionary of chamption stats
                #for statName in participant['championStats']:
                #    participantinfo[f'Champ{participantid}_{statName}'] = participant['championStats'][statName]

            newdict = dict()
            newdict.update(teaminfo.copy())
            newdict.update(participantinfo.copy())

            overalldict[frameid] = newdict.copy()

            frameid += 1

        evenmoreoverall = dict()
        evenmoreoverall['winningteam'] = matchinfo['WinningTeam']
        evenmoreoverall['frames'] = overalldict.copy()

        mactchdict[match['gameid']] = evenmoreoverall.copy()

with open("ReducedMatchesProcessed2-3-OneMatch.json", "w") as outfile:
    json.dump(mactchdict, outfile, separators=(',', ':'))
