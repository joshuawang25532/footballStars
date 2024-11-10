import numpy
import pandas as pd
import time

# Aggregates lifetime data from goalscorers.csv

dSet = {}
start_time = time.time()

def update(df):
    global dSet
    name = df['scorer'].iloc[0]

    # Remove missing data
    # Some rows don't have names
    if type(name) == numpy.float64:
        return

    if name not in dSet.keys():
        dSet[name] = {
            'total_goals': 0,
            'matches': 0,
            'latest_match': 0,
            'home_goals': 0,
            'away_goals': 0,
            'own_goals': 0,
            'penalty_goals': 0
        }

    dSet[name]['total_goals'] += 1
    if dSet[name]['latest_match'] != df['date'].iloc[0]:
        dSet[name]['latest_match'] = df['date'].iloc[0]
        dSet[name]['matches'] += 1
    if df['team'].iloc[0] == df['home_team'].iloc[0]:
        dSet[name]['home_goals'] += 1
    else:
        dSet[name]['away_goals'] += 1
    if df['own_goal'].iloc[0] == 1:
        dSet[name]['own_goals'] += 1
    if df['penalty'].iloc[0] == 1:
        dSet[name]['penalty_goals'] += 1


for df in pd.read_csv('goalscorers.csv', chunksize=1):
    update(df)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

with open('output.txt', 'w') as file:
    for i in dSet.keys():
        try:
            file.write(i + ": " + str(dSet[i]) + "\n")
        except:
            print("Error here!" + "\n")
            print(i)
            print(dSet[i])

df = pd.DataFrame.from_dict(dSet, orient='index').reset_index()

df = df.rename(columns={'index': 'playerName'})

df.to_csv('players_stats.csv', index=False)