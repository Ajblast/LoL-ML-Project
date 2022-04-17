import json

match0 = open("Matches0.json", "r")
match1 = open("Matches1.json", "r")
match2 = open("Matches2.json", "r")
match3 = open("Matches3.json", "r")

print("Load Match 0")
match0json = json.load(match0)
print("Load Match 1")
match1json = json.load(match1)
print("Load Match 2")
match2json = json.load(match2)
print("Load Match 3")
match3json = json.load(match3)

match0.close()
match1.close()
match2.close()
match3.close()

matches = []
matches.extend(match0json)
matches.extend(match1json)
matches.extend(match2json)
matches.extend(match3json)

print("Write Matches")
with open("Matches.json", "w") as outfile:
    json.dump(matches, outfile, separators=(',', ':'))
