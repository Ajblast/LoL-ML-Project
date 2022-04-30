set apiKey=%1
ECHO Fetching Match IDS 
python FetchMatchIds.py %apiKey%
ECHO Retriving Timeline Data - First quarter a
python GetMatchTimeData.py %apiKey% -1
ECHO Processing Timeline Data 
python MatchTimelinePreProcessor.py
ECHO Training Model 
python ModelTraining.py 8 2 .25 .01