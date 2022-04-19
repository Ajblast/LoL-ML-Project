import torch
import json
import random
import pandas as pd
import numpy as np

model = torch.load("TestModel.pt")

#Load the matches
matches = None
with open("ReducedMatchesProcessed2-3.json", "r") as infile:
    matches = json.load(infile)

#Get the match data frames
matchDataFrames = []
for matchid in matches:
    match = matches[matchid]
    winningTeam = match['winningteam']
    frames = match['frames']

    matchDataFrame = pd.DataFrame(frames).T
    matchDataFrame['winningteam'] = winningTeam

    matchDataFrames.append(matchDataFrame)
del matches

#Get the training and test set
indices = range(len(matchDataFrames))
trainset = random.sample(indices, k = int(len(indices) * .8))
testset = [x for x in indices if x not in trainset]

trainset = [matchDataFrames[i] for i in trainset]
testset = [matchDataFrames[i] for i in testset]

correctPred = 0
totalPred = 0
with torch.no_grad():
    for match in testset:
        x = match.loc[:, match.columns != 'winningteam']
        y = match.loc[:, 'winningteam'].replace([100, 200], [0, 1])
        x = torch.tensor(x.values, dtype=torch.float32)
        y = torch.tensor(y.values, dtype=torch.long)
        output = model(x)
        output = torch.exp(output)
        #print(output)

        winningteam = -1
        if(output[0,-1] >= .5):
            winningTeam = 0
        else:
            winningTeam = 1
        
        if(y[-1] == winningTeam):
            correctPred += 1
        totalPred += 1

predictionRate = correctPred / totalPred
print(f"Correct Prediction Rate: {predictionRate}")
