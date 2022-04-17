import torch.nn as nn
import torch.nn.functional as F

class LSTMModel(nn.Module):
    def __init__(self, num_classes, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.num_classes = num_classes  #number of classes
        self.num_layers = num_layers    #number of layers
        self.input_size = input_size    #input size
        self.hidden_size = hidden_size  #hidden state

        #LSTM model
        self.lstm = nn.LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers)
        #Final linear layer
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        #Go through the lstm model
        output, (hn, cn) = self.lstm(x)

        #Translate from LSTM to linear layer to reduce to the classifications
        output = self.fc(output.view(-1, self.hidden_size))

        #Translate the arbitrary linear layer outputs into the actual classification probabilities
        output = F.log_softmax(output, dim=1)

        return output