import progressbar
import json
import pandas as pd
import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim

import LSTMModel

#Load the matches
matches = None
with open("MatchesProcessed.json", "r") as infile:
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


#Create the LSTM model
model = LSTMModel.LSTMModel(2, 392, 32, 2)
loss_function = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

totalloss = []

#Train
widgets = ['[', progressbar.Counter(format='%(value)d/%(max_value)d'), ']', progressbar.Timer(format="Elapsed Time: %(elapsed)s"), ']', progressbar.Bar('*')]
for i in progressbar.progressbar(range(len(trainset)), widgets=widgets):
    match = trainset[i]

    # Step 1. Remember that Pytorch accumulates gradients.
    # We need to clear them out before each instance
    model.zero_grad()

    # Step 2. Get our inputs ready for the network, that is, turn them into Tensors.
    x = match.loc[:, match.columns != 'winningteam']
    y = match.loc[:, 'winningteam'].replace([100, 200], [0, 1])

    x = torch.tensor(x.values, dtype=torch.float32)
    y = torch.tensor(y.values, dtype=torch.long)

    # Step 3. Run our forward pass.
    output = model(x)

    # Step 4. Compute the loss, gradients, and update the parameters by calling optimizer.step()
    loss = loss_function(output, y)
    totalloss.append(loss.item())
    loss.backward()
    optimizer.step()

    if i % int(len(trainset) * .1) == 0:
        print(f"\nEpoch {i}, Loss: {np.average(np.asarray(totalloss)):.2f}")


torch.save(model, "TestModel.pt")