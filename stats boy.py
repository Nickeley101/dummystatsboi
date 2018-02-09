from lxml import html
import requests
#Pull sommoner names
f = open('names.txt','r')
content = f.read()
content = content.split()
#count names
numname = len(content)
for x in range(0,numname):
    summs = content[x]
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
    lose = tree.xpath('//span[@class="losses"]/text()')
    wins = wins[0]
    lose = lose[0]
    #print it
    final = summs + '\n' + rank + "," + lp + ","+ wr+ ","+ wins+ ","+ lose
    print(final)