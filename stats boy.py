from lxml import html
import requests
#Ask for who to pull
summs = str(input("Who? "))
#Pull HTML from op.gg if on NA
whosite = 'http://na.op.gg/summoner/userName=' + summs
page = requests.get(whosite)
#turn into goodo boyo tree
tree = html.fromstring(page.content)
#Tell me rank boyo
rank = tree.xpath('//span[@class="tierRank"]/text()')
#Tell me LP
lp = tree.xpath('//span[@class="LeaguePoints"]/text()')
print(lp)
final = ' '.join(lp)
print(final)