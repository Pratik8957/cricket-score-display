import requests
import pandas as pd

url = "https://api.cricapi.com/v1/currentMatches?apikey=09a82d34-1169-435f-896a-ab8d33ce56de"

response = requests.get(url)
data = response.json()

matches = []

for match in data['data']:
    matches.append({
        "Match": match['name'],
        "Status": match['status']
    })

df = pd.DataFrame(matches)

print(df)