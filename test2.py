import json
import sys

matchCount = int(sys.argv[1])

#Load the matches
matches = None
with open("MatchesProcessed.json", "r") as infile:
    matches = json.load(infile)

    newmatches = dict()

    counter = 0
    for matchid in matches:
        if counter == matchCount:
            break
        newmatches[matchid] = matches[matchid]
        counter += 1

    matches = newmatches


with open("TestProcessed.json", "w") as outfile:
    json.dump(matches, outfile)

