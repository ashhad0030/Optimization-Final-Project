import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('all_data/players_22.csv')
liv_val = df.loc[df['club_name'] == 'Liverpool']
liv_val.to_csv('Liverpool_FIFA_22.csv')

url = 'https://www.fifaindex.com/teams/fifa22/?league=13'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
teams = soup.findChildren('table')[0]

rows = teams.findChildren(['th', 'tr'])

attributes = [[] for i in range(6)]
for row in rows:
    cells = row.findChildren('td')
    count = 0
    for cell in cells:
        value = cell.string
        if value is not None:
            attributes[count%6].append(value)
            count = (count+1)%6
    name, league, attack, mid, defence, ovr = attributes

data = {'Name': name, 'Att': attack, 'Mid': mid, 'Def': defence, 'OVR': ovr}
team_df = pd.DataFrame(data)
team_df.to_csv('Team_Ratings.csv')