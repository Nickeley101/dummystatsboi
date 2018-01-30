from lxml import html
import requests
#Ask for who to pull, eventually replace this with a text file and spit out stats for every name in the file
summs = str(input("Who?(type summoner name) "))
#Pull HTML from op.gg if on NA
whosite = 'http://na.op.gg/summoner/userName=' + summs
page = requests.get(whosite)
#turn into goodo boyo tree
tree = html.fromstring(page.content)
#Tell me rank boyo
rank = tree.xpath('//span[@class="tierRank"]/text()')
#format the list item as a str
rank = rank[0]
#Tell me LP
lp = tree.xpath('//span[@class="LeaguePoints"]/text()')
#remove whitespace
lp = lp[0].strip()
#tell me win rate stuffs
#pull wr
wr = tree.xpath('//span[@class="winratio"]/text()')
wr = wr[0]
#pull wins and losses
wins = tree.xpath('//span[@class="wins"]/text()')
wins = wins[0]
lose = tree.xpath('//span[@class="losses"]/text()')
lose = lose[0]
#print it
print(summs)
print(rank,",", lp,",",wr,",",wins,",",lose)