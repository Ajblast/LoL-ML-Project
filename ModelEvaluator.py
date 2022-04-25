import torch
import json
import random
import pandas as pd
import numpy as np

print("Load Model")
model = torch.load("TestModel.pt")

print("\nLoad Train Test Set")
trainset = []
testset = []
with open("TrainingSet.json", "r") as infile:
    trainset = json.load(infile)
with open("TestingSet.json", "r") as infile:
    testset = json.load(infile)

print("\nModel Evaluation:")
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
        for prediction in x:
            if(prediction[0] >= .5):
                winningTeam = 0
            else:
                winningTeam = 1

            if(y[-1] == winningTeam):
                correctPred += 1
            totalPred += 1

predictionRate = correctPred / totalPred
print(f"Correct Prediction Rate: {predictionRate}")
