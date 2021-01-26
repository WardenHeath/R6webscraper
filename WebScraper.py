# link = https://siege.gg/matches/2
# Uses Request and BS4
# note: Alpha = left = top of stat board
#       Bravo = right = bottom of stat board
from typing import BinaryIO

import requests
from bs4 import BeautifulSoup
import re
import csv
# TODO: CSV writes properly, need to add Win/lose functionality
# Using request module, we use the get function provided
# provided to access the web page
url = "https://siege.gg/matches/3859"
page = requests.get(url)

# print(result.status_code)
src = page.content
Soup = BeautifulSoup(page.content, 'html.parser')
# getting the team scores
teamAScoreHTML = Soup.find('div', class_='col-12 col-md match__overview align-self-stretch team--a')
teamBScoreHTML = Soup.find('div', class_='col-12 col-md match__overview align-self-stretch team--b')
# removes whitespace from scrape and store in new variable
teamAScore = ' '.join(teamAScoreHTML.text.split())
teamBScore = ' '.join(teamBScoreHTML.text.split())
# filters the names of the teams out
teamAlphaScoreInt = int(re.sub('\D', '', teamAScore).strip())
teamBetaScoreInt = int(re.sub('\D', '', teamBScore).strip())

tableClass = Soup.find('div', {"class": "row row--padded match__player-stats"})
table = tableClass.find("table")

print("Team Alpha Score: ") 
print(teamAlphaScoreInt)
print("Team Beta Score: ")
print(teamBetaScoreInt)

if teamAlphaScoreInt > teamBetaScoreInt:
    TeamAWin = 1
    TeamBwin = 0
    draw = 0
elif teamBetaScoreInt > teamAlphaScoreInt:
    TeamBwin = 1
    TeamAwin = 0
    draw = 0
else:
    Draw = 1




# Finds all rows and adds to outputrows array
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
# Removes the Empty value
output_rows.pop(0)

if TeamAWin == 1 and TeamBwin == 0 and draw == 0:
    print("team A wins")
elif TeamAWin == 0 and TeamBwin == 1 and draw == 0:
    print("team B wins")
else:
    print("its a draw")

print("\nRow data is: ")
for row in output_rows:
    for val in row:
        print '{:4}'.format(val),
    print


#Uncomment when done with rest of code/change so that it adds to csv rather than overwrites
#with open('output.csv', 'wb') as csvfile:
    #writer = csv.writer(csvfile)
    #writer.writerows(output_rows)

# if tASInt > tBSInt:
# alphaWin = 1
# betaWin = 0
# else:
# alphaWin = 0
# betaWin = 1

# print("Team A win = " + repr(alphaWin) + "\nTeam B win = " + repr(betaWin))

# print(tASInt)
# print(tBSInt)
