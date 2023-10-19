from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

games = read_csv("valorant_games.csv")
X = games.drop(columns=["win"])
y = games["win"]

model = DecisionTreeClassifier()
model.fit(X.values, y.values)

MapInput = str(input("\nInsert the map name: ")).lower()
A1Input = str(input("\nInsert the first agent: ")).lower()
A2Input = str(input("\nInsert the second agent: ")).lower()
A3Input = str(input("\nInsert the third agent: ")).lower()
A4Input = str(input("\nInsert the fourth agent: ")).lower()
A5Input = str(input("\nInsert the last agent: ")).lower()

maps_to_number = {
    "ascent": 1,
    "bind": 2,
    "breeze": 3,
    "haven": 4,
    "lotus": 5,
    "split": 6,
    "sunset": 7,
}

agents_to_number = {
    "astra": 1,
    "breach": 2,
    "brimstone": 3,
    "chamber": 4,
    "cypher": 5,
    "deadlock": 6,
    "fade": 7,
    "gekko": 8,
    "harbor": 9,
    "jett": 10,
    "kayo": 11,
    "killjoy": 12,
    "neon": 13,
    "omen": 14,
    "phoenix": 15,
    "raze": 16,
    "reyna": 17,
    "sage": 18,
    "skye": 19,
    "sova": 20,
    "viper": 21,
    "yoru": 22,
}


prevision = model.predict(
    [
        [
            maps_to_number[MapInput],
            agents_to_number[A1Input],
            agents_to_number[A2Input],
            agents_to_number[A3Input],
            agents_to_number[A4Input],
            agents_to_number[A5Input],
        ]
    ]
)

if prevision == 1:
    print("\n\nGreat news: you're going to win!\n")
elif prevision == 2:
    print("\n\nBad news for your team: you're going to lose...\n")
else:
    print("\n\nOoops, something went wrong...\n")