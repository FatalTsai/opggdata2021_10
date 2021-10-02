import http.client
import re
from bs4 import BeautifulSoup
import html_to_json
import os
import json



conn = http.client.HTTPSConnection("www.op.gg")
payload = ''
headersForID = {# the ID of summoners in OPGG 
  'cookie': 'customLocale=en_US;'
}
conn.request("GET", "/summoner/userName=dingjimeinv", payload, headersForID)
resForRawID = conn.getresponse()
IDRawData = resForRawID.read()
# print(data.decode("utf-8"))


# https://regex101.com/r/w26nnn/1
regexID = r"<button class=\"Button SemiRound Blue\" id=\"SummonerRefreshButton\" onclick=\"\$\.OP\.GG\.summoner\.renewBtn\.start\(this, '\d+'\);\" style=\"position: relative;\">"
matchesID = re.finditer(regexID, IDRawData.decode("utf-8"), re.MULTILINE)
OpggID=""


for matchNum, match in enumerate(matchesID, start=1):
    
    # print ("raw Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


    regexpureID = r"\d+"
    #https://regex101.com/r/tZJPyN/1/

    matches = re.finditer(regexpureID, str(match.group()), re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        
    #     for groupNum in range(0, len(match.groups())):
    #         groupNum = groupNum + 1
            
    #         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
        OpggID = str(match.group()) 


# print(ans)
lastInfo = "9999999999"
matchData : dict()

def askfor20(lastInfo,matchData):
    headers = {
    'accept-language': 'en-US,e:n;q=0.9',
    'cookie': 'customLocale=en_US;'
    }
    # conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo=9999999999&summonerId="+OpggID, payload, headers)
    # conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo=1632637821&summonerId="+OpggID, payload, headers)
    conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo="+lastInfo+"&summonerId="+OpggID, payload, headers)


    res = conn.getresponse()
    # data = res.read().decode("utf-8")
    data = res.read()
    print('lastinfo :',str(data[12:22] )) #lastinfo
    # print(str(data[31:-2] )) #html
    lastInfo = str(data[12:22] )
    htmlData = str(data[31:-4])
    htmlData = htmlData.replace("\\t", '')
    htmlData = htmlData.replace("\\n", '')
    htmlData = htmlData.replace("\\\\", '')
    htmlData = htmlData.replace(">\\", '>')
    htmlData = htmlData.replace("\\'", '>')
    htmlData = htmlData[2:-1]
    # print(htmlData)
    # print(html_to_json.convert_tables(htmlData) )

    # print(lastInfo)



    soup = BeautifulSoup(htmlData, 'html.parser')
    with open("YA2UD.html", "w") as out_file:
        out_file.write(soup.prettify()) 



    with open("YA2UD.html", "r") as f:
        data =  str(f.read())

    html_string = """<head>
        <title>Test site</title>
        <meta charset="UTF-8"></head>"""

    # print(type(data))
    #output_json = html_to_json.convert(data)
    # print(output_json)

    # print(soup.prettify() )
    # print (html_to_json.convert_tables(htmlData ))

    # with open('data.json', 'w', encoding='utf-8') as f:
    #     json.dump(html_to_json.convert(data), f, ensure_ascii=False, indent=2)



    raw : object = html_to_json.convert(data)
    # with open('data.json', 'r', encoding='utf-8') as f:
    #     raw = json.load(f)
    exactData(raw,matchData)
    # print(type(lastInfo))
    print( int(lastInfo[2:-1]) - 30000)
    # print(type(tmp))

    # print("tmp = ",tmp)
    # lastInfo = str(tmp)
    askfor20(str(int(lastInfo[2:-1]) - 30000),matchData)


def exactData(raw,matchData):
    matches = raw["div"][0]["div"]

    for match in matches[:]:
        matchInfo = dict()

        # print( "gameID  :",match["div"][0]["_attributes"]["data-game-id"] )  # gameID
        matchInfo["gameID"]=match["div"][0]["_attributes"]["data-game-id"] 
        
    #     print( "win or lose?    :",match["div"][0]["_attributes"]["data-game-result"] )  # win or lose?
        matchInfo["gameResult"]=match["div"][0]["_attributes"]["data-game-time"]

        # print( "gameTime_int    :",match["div"][0]["_attributes"]["data-game-time"] )  # gameTime_int
        matchInfo["gameTime_int"]=match["div"][0]["_attributes"]["data-game-result"]
        print(matchInfo)

    #     print( match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"])  #GameType
        matchInfo["GameType"]=match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"]

    #     print( match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]) ## gameTime_string
        matchInfo["gameTime_string"]=match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]

    #     print( match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]) #GameLength
        matchInfo["GameLength"]=match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]

        
    #     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][0]["img"][0]['_attributes']["alt"])#D_SummonerSpell
        matchInfo["D_SummonerSpell"]=match["div"][0]["div"][0]["div"][1]['div'][1]["div"][0]["img"][0]['_attributes']["alt"]
    #     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][1]["img"][0]['_attributes']["alt"])#F_SummonerSpell
        matchInfo["F_SummonerSpell"]=match["div"][0]["div"][0]["div"][1]['div'][1]["div"][1]["img"][0]['_attributes']["alt"]

    #     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][0]["img"][0]["_attributes"]["alt"]) #main_Rune
        matchInfo["main_Rune"]=match["div"][0]["div"][0]["div"][1]["div"][2]["div"][0]["img"][0]["_attributes"]["alt"]

    #     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][1]["img"][0]["_attributes"]["alt"]) #second_Rune
        matchInfo["second_Rune"]=match["div"][0]["div"][0]["div"][1]["div"][2]["div"][1]["img"][0]["_attributes"]["alt"]

    #     print("kill :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][0]["_value"] )#kill
        matchInfo["kill"]=match["div"][0]["div"][0]["div"][2]["div"][0]["span"][0]["_value"]

    #     print("Death :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][1]["_value"] )#Death
        matchInfo["Death"]=match["div"][0]["div"][0]["div"][2]["div"][0]["span"][1]["_value"]

    #     print("Assist :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][2]["_value"] )#Assist
        matchInfo["Assist"]=match["div"][0]["div"][0]["div"][2]["div"][0]["span"][2]["_value"]


    #     print("KDARatio :",match["div"][0]["div"][0]["div"][2]["div"][1]["span"][0]["_value"])
        matchInfo["KDARatio"]=match["div"][0]["div"][0]["div"][2]["div"][1]["span"][0]["_value"]

        if(len( match["div"][0]["div"][0]["div"][2]["div"]) >2):
    #         print("Badge1 :", match["div"][0]["div"][0]["div"][2]["div"][2]["span"][0]["_value"] )
            matchInfo["Badge1"]=match["div"][0]["div"][0]["div"][2]["div"][2]["span"][0]["_value"]
        if(len( match["div"][0]["div"][0]["div"][2]["div"]) >3):
    #         print("Badge2 :",match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"])
            matchInfo["Badge1"]=match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"]



        #print(match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]) #champion
        matchInfo["champion"]=match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]
        
    #     print(match["div"][0]["div"][0]["div"][3]["div"][0]["_value"])#level
        matchInfo["level"]=match["div"][0]["div"][0]["div"][3]["div"][0]["_value"]
    #     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"])#detail cs info
        matchInfo["detail_cs_info"]=match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"]
    #     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]) #cs and avg_cs_per_mins
        matchInfo["cs"]=match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]
    #     print(match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]) #Kill Participation
        matchInfo["Kill_Participation"]=match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]

        if(len(match["div"][0]["div"][0]["div"][3]["div"]) > 3 ):
    #         print(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]) #Tier Average
            matchInfo["Tier_Average"]= match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]

       

    #     print(list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][5].keys() )[1]) #identiy if the item is exist or not

        for target in range(7):
            if(  list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target].keys() )[1] == 'img'):
                # print(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"])
                matchInfo["item"+str(target)]= match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"]




        if(len(match["div"][0]["div"][0]["div"][4]["div"] )> 1):
            # print(match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]) #Control Ward
            matchInfo["Control_Ward"]=match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]
        for teammate in range(5):
    #         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]) #teammate1 champion
    #         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"])#teammate1 id
            matchInfo["teammate_champion"+str(teammate)]=match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]
            matchInfo["teammate_id"+str(teammate)]=match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"]

        
        for enermy in range(5):
            # print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]) 
            # print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"])
            matchInfo["enermy_champion"+str(enermy)]=match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]
            if(  list(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1].keys())[0]== 'a'):
                matchInfo["enermy_id"+str(enermy)]=match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"]


        matchData[ matchInfo["gameID"] ] = matchInfo
    with open("YA2UD.json", "w") as f:
        json.dump(matchData, f, ensure_ascii=False, indent=2)

    return matchData


askfor20(lastInfo,dict())