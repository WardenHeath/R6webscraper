# link = https://siege.gg/matches/2
# Uses Request and BS4
# note: Alpha = left = top of stat board
#       Bravo = right = bottom of stat board
from __future__ import print_function
from typing import BinaryIO

import requests
from bs4 import BeautifulSoup

import re
import csv
# TODO: 
# Using request module, we use the get function provided
# provided to access the web page
matchNumber = input("Enter last match number from siege.gg: ")
matchNumber_int = int(matchNumber)
x = 1
while x <= matchNumber_int:
    url = "https://siege.gg/matches/"
    url +=`x`
    page = requests.get(url)
    print(url)
    try:
        # print(result.status_code)
        src = page.content
        Soup = BeautifulSoup(page.content, 'html.parser')

        print("\nFound match ", x,". Writing to CSV...")

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


        if TeamAWin == 1 and TeamBwin == 0 and draw == 0:
        # print("team A wins")
            #Updating Winners and losers if team A wins
            player1data = output_rows[0]
            player1data.append("Win")
            player2data = output_rows[1]
            player2data.append("Win")
            player3data = output_rows[2]
            player3data.append("Win")
            player4data = output_rows[3]
            player4data.append("Win")
            player5data = output_rows[4]
            player5data.append("Win")
            player6data = output_rows[5]
            player6data.append("Loss")
            player7data = output_rows[6]
            player7data.append("Loss")
            player8data = output_rows[7]
            player8data.append("Loss")
            player9data = output_rows[8]
            player9data.append("Loss")
            player10data = output_rows[9]
            player10data.append("Loss")
        elif TeamAWin == 0 and TeamBwin == 1 and draw == 0:
        # print("team B wins")
            player1data = output_rows[0]
            player1data.append("Loss")
            player2data = output_rows[1]
            player2data.append("Loss")
            player3data = output_rows[2]
            player3data.append("Loss")
            player4data = output_rows[3]
            player4data.append("Loss")
            player5data = output_rows[4]
            player5data.append("Loss")
            player6data = output_rows[5]
            player6data.append("Win")
            player7data = output_rows[6]
            player7data.append("Win")
            player8data = output_rows[7]
            player8data.append("Win")
            player9data = output_rows[8]
            player9data.append("Win")
            player10data = output_rows[9]
            player10data.append("Win")
        else:
            #print("its a draw")
            player1data = output_rows[0]
            player1data.append("Draw")
            player2data = output_rows[1]
            player2data.append("Draw")
            player3data = output_rows[2]
            player3data.append("Draw")
            player4data = output_rows[3]
            player4data.append("Draw")
            player5data = output_rows[4]
            player5data.append("Draw")
            player6data = output_rows[5]
            player6data.append("Draw")
            player7data = output_rows[6]
            player7data.append("Draw")
            player8data = output_rows[7]
            player8data.append("Draw")
            player9data = output_rows[8]
            player9data.append("Draw")
            player10data = output_rows[9]
            player10data.append("Draw")

        #print("\nRow 1 data is")
        #print(output_rows[0][1])
        matchMaps = Soup.find_all('td', class_='ban__map')
        matchrow = []
        for matchmap in matchMaps:
            matchrow.append(matchmap.text)

        PlayedMap = matchrow[6]

        player1data = output_rows[0]
        player1data.append(PlayedMap)
        player2data = output_rows[1]
        player2data.append(PlayedMap)
        player3data = output_rows[2]
        player3data.append(PlayedMap)
        player4data = output_rows[3]
        player4data.append(PlayedMap)
        player5data = output_rows[4]
        player5data.append(PlayedMap)
        player6data = output_rows[5]
        player6data.append(PlayedMap)
        player7data = output_rows[6]
        player7data.append(PlayedMap)
        player8data = output_rows[7]
        player8data.append(PlayedMap)
        player9data = output_rows[8]
        player9data.append(PlayedMap)
        player10data = output_rows[9]
        player10data.append(PlayedMap)

        #print("\nRow data is: ")
        #for row in output_rows:
            #for val in row:
            # print '{:4}'.format(val),
        #  print

        #Uncomment when done with rest of code/change so that it adds to csv rather than overwrites
        with open('output.csv', 'ab') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(output_rows)
    except:
        print("No match data was found at match ", x)
    finally:
        x += 1
