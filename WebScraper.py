# link = https://siege.gg/matches/2
# Uses Request and BS4
# note: Alpha = left = top of stat board
#       Bravo = right = bottom of stat board
import requests
from bs4 import BeautifulSoup
import re
# Using request module, we use the get function provided
# provided to access the web page
url = "https://siege.gg/matches/100"
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
tASInt = int(re.sub('\D', '', teamAScore).strip())
tBSInt = int(re.sub('\D', '', teamBScore).strip())

if tASInt > tBSInt:
    alphaWin = 1
else:
    alphaWin = 0

print(alphaWin)

# print(tASInt)
# print(tBSInt)
