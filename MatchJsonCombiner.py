import json
import sys

quarters = int(sys.argv[1])

matches = []
for i in range(quarters):
    print(f"Load Match {i}")
    matchData = open(f"Matches{i + 1}.json", "r")
    matchjson = json.load(matchData)
    matchData.close()

    matches.extend(matchjson)

print("Write Matches")
with open("Matches.json", "w") as outfile:
    json.dump(matches, outfile, separators=(',', ':'))
