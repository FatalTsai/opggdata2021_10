import http.client
import re
from bs4 import BeautifulSoup
import html_to_json
import os
import json
from urllib.parse import unquote
import urllib
import time
import csv


# tmp = '%EB%B3%91%EC%94%AC%EA%B0%99%EC%9D%80%EA%B2%8C%EC%9E%84'

# from urllib.parse import unquote

# tmp = unquote(tmp)

# print(tmp)
conn = http.client.HTTPSConnection("www.op.gg")
summonerName  :str  = ""
OpggID=""
payload = ''
playerStat: dict()

def getOpggID(summonerName):
    headersForID = {# the ID of summoners in OPGG 
    'cookie': 'customLocale=en_US;'
    }
    # print(" request.....> ","/summoner/userName="+summonerName, payload, headersForID)

    conn.request("GET", "/summoner/userName="+urllib.parse.quote(str(summonerName)), payload, headersForID)
    # conn.request("GET", "/summoner/userName="+urllib.parse.quote("아이마스+타카네"), payload, headersForID)

    resForRawID = conn.getresponse()
    IDRawData = resForRawID.read()
    # print(IDRawData.decode("utf-8"))

    # https://regex101.com/r/w26nnn/1
    regexID = r"<button class=\"Button SemiRound Blue\" id=\"SummonerRefreshButton\" onclick=\"\$\.OP\.GG\.summoner\.renewBtn\.start\(this, '\d+'\);\" style=\"position: relative;\">"
    matchesID = re.finditer(regexID, IDRawData.decode("utf-8"), re.MULTILINE)


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
            return str(match.group()) 


# print(ans)
lastInfo = "9999999999"
matchData : dict()

def parsePureID(oldID):
    regex = r"userName=.*"

    oldID = unquote(oldID)
    matches = re.finditer(regex, oldID, re.MULTILINE)
    # https://regex101.com/r/TvPjvR/1
    for matchNum, match in enumerate(matches, start=1):
        
        # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        return (match.group().replace("userName=","")).replace("+"," ")
        
        

def askfor20(lastInfo,matchData):
    headers = {
    'accept-language': 'en-US,e:n;q=0.9',
    'cookie': 'customLocale=en_US;'
    }
    # conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo=9999999999&summonerId="+OpggID, payload, headers)
    # conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo=1632637821&summonerId="+OpggID, payload, headers)
    conn.request("GET", "/summoner/matches/ajax/averageAndList/startInfo="+str(lastInfo)+"&summonerId="+str(OpggID), payload, headers)


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
    if(htmlData.find('GameItemWrap' )== -1):
        print(htmlData.find('GameItemWrap' ))
        print(summonerName," data end")
        return matchData


    soup = BeautifulSoup(htmlData, 'html.parser')
    with open("tmp.html", "w") as out_file:
        out_file.write(soup.prettify()) 


    with open("tmp.html", "r") as f:
        data =  str(f.read())



    # print(type(data))
    #output_json = html_to_json.convert(data)
    # print(output_json)

    # print(soup.prettify() )
    # print (html_to_json.convert_tables(htmlData ))

    with open('rawdata.json', 'w', encoding='utf-8') as f:
        json.dump(html_to_json.convert(data), f, ensure_ascii=False, indent=2)



    raw : object = html_to_json.convert(data)
    # with open('data.json', 'r', encoding='utf-8') as f:
    #     raw = json.load(f)
    exactData(raw,matchData)
    # print(type(lastInfo))
    # print( int(lastInfo[2:-1]) - 10000)
    # print(type(tmp))

    # print("tmp = ",tmp)
    # lastInfo = str(tmp)
    askfor20(str(int(lastInfo[2:-1]) - 50000),matchData)




def exactData(raw,matchData):
    matches = raw["div"][0]["div"]
    fishFiter = False
    for match in matches[:]:
        matchInfo = dict()
        # print( "gameID  :",match["div"][0]["_attributes"]["data-game-id"] )  # gameID
        # if(fishFiter):
        matchInfo["gameID"]=match["div"][0]["_attributes"]["data-game-id"] 
        
    #     print( "win or lose?    :",match["div"][0]["_attributes"]["data-game-result"] )  # win or lose?
        if(fishFiter):
            matchInfo["gameTime_int"]=match["div"][0]["_attributes"]["data-game-time"]

        # print( "gameTime_int    :",match["div"][0]["_attributes"]["data-game-time"] )  # gameTime_int
        matchInfo["gameResult"]=match["div"][0]["_attributes"]["data-game-result"]
        # print(matchInfo)

    #     print( match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"])  #GameType
        if(list(match["div"][0]["div"][0]["div"][0].keys())[1] == "div" ):
            matchInfo["GameType"]=match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"]
        elif(match["div"][0]["div"][0]["div"][0] != None):  ##Game hasn>t been updated on OP.GG
            print(match["div"][0]["div"][0]["div"][0])
            matchInfo["GameType"] = match["div"][0]["div"][0]["div"][0]["_value"]
            matchData[ matchInfo["gameID"] ] = matchInfo
            with open("output/"+str(playerStat["team"])+"/"+str(playerStat["player"])+"/"+str(summonerName)+".json", "w",encoding="utf8") as f:
                json.dump(matchData, f, ensure_ascii=False, indent=2)
            return matchData
        else: 
            matchInfo["GameType"] = "empty"


    #     print( match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]) ## gameTime_string
        matchInfo["gameTime_string"]=match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]

    #     print( match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]) #GameLength
        matchInfo["GameLength"]=match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]

        
    #     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][0]["img"][0]['_attributes']["alt"])#D_SummonerSpell
        if(fishFiter):
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
        else:
             matchInfo["Badge1"]="empty"
        if(len( match["div"][0]["div"][0]["div"][2]["div"]) >3):
    #         print("Badge2 :",match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"])
            matchInfo["Badge2"]=match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"]
        else:
            matchInfo["Badge2"]="empty"


        #print(match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]) #champion
        matchInfo["champion"]=match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]
        
    #     print(match["div"][0]["div"][0]["div"][3]["div"][0]["_value"])#level
        if(fishFiter):
            championLevel = match["div"][0]["div"][0]["div"][3]["div"][0]["_value"]
            levelNumeric_filter = filter(str.isdigit, championLevel)
            levelNumeric_string = "".join(levelNumeric_filter)
            matchInfo["level"]=levelNumeric_string

        #     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"])#detail cs info
            # matchInfo["detail_cs_info"]=match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"]
            detail_cs_info = match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"]
        #     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]) #cs and avg_cs_per_mins

            matchInfo["minion"] = re.sub('[^0-9]','',re.search(r"minion.*\+", detail_cs_info,re.M|re.I).group())
            # Removing non numeric characters from a string https://stackoverflow.com/questions/17336943/removing-non-numeric-characters-from-a-string
            # https://regex101.com/r/rZaHO1/1

            matchInfo["monster"] = re.sub('[^0-9]','',re.search(r"\+.*monster.*<br>", detail_cs_info,re.M|re.I).group())



            matchInfo["cs_total"]=re.sub(r'\(.*\)','',match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]).strip()
            matchInfo["cs_per_minutes"] = re.search(r'[+-]?([0-9]*[.])?[0-9]+', re.search(r'\<br\>CS.*per.*minute:.*', detail_cs_info,re.M|re.I).group() ,re.M|re.I).group()
            ## Regular expression for floating point numbers https://stackoverflow.com/questions/12643009/regular-expression-for-floating-point-numbers


        #     print(match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]) #Kill Participation
            # matchInfo["Kill_Participation"]=match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]
            matchInfo["Control_Ward"]="".join(filter(str.isdigit,match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]) ) ## erase non-digit char

        # print(match["div"][0]["div"][0]["div"][3]["div"][3]["b"])
        # print(len(list(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0].keys())) >0 )
        if(len(match["div"][0]["div"][0]["div"][3]["div"]) > 3  and len(list(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0].keys())) >0   ):
    #         print(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]) #Tier Average
            matchInfo["Tier_Average"]= match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]
        else:
            matchInfo["Tier_Average"]="empty"

       

    #     print(list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][5].keys() )[1]) #identiy if the item is exist or not
        if(fishFiter):
            for target in range(7):
                if(  list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target].keys() )[1] == 'img'):
                    # print(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"])
                    matchInfo["item"+str(target)]= match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"]
                else:
                    matchInfo["item"+str(target)]="empty"
            if(len(match["div"][0]["div"][0]["div"][4]["div"] )> 1):
                # print(match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]) #Control Ward
                matchInfo["Control_Ward"]="".join(filter(str.isdigit,match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]) )## erase non-digit char


        else:
            matchInfo["Control_Ward"]="empty"
        for teammate in range(len(match["div"][0]["div"][0]["div"][5]["div"][0]["div"])):
    #         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]) #teammate1 champion
    #         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"])#teammate1 id
            matchInfo["teammate_champion"+str(teammate)]=match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]
            if( list(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1].keys())[1] =='a' ):
                matchInfo["teammate_id"+str(teammate)]=parsePureID( match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"])
            else:
                matchInfo["teammate_id"+str(teammate)]="empty"

        
        for enermy in range(5):
            # print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]) 
            # print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"])
            # print( match["div"][0]["div"][0]["div"][5]["div"][1])
            

            if(len(list(match["div"][0]["div"][0]["div"][5]["div"][1].keys()) ) < 2 ):
                matchInfo["enermy_champion"+str(enermy)]="empty"
                matchInfo["enermy_id"+str(enermy)]="empty"
                break



            matchInfo["enermy_champion"+str(enermy)]=match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]
            # print("keys = ",list(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1].keys()))
            if(  list(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1].keys())[1]== 'a'):
                # div[0].div[0].div[0].div[0].div[5].div[1].div[0].div[1]._attributes
                matchInfo["enermy_id"+str(enermy)]=parsePureID( match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"] )
            else:
                matchInfo["enermy_id"+str(enermy)]="empty"


        matchData[ matchInfo["gameID"] ] = matchInfo

    if(os.path.exists('output/') == False):
        os.makedirs('output')
    if(os.path.exists("output/"+playerStat["team"]) == False):
        os.makedirs("output/"+playerStat["team"])
    if(os.path.exists("output/"+playerStat["team"]+"/"+playerStat["player"]) == False):
        os.makedirs("output/"+playerStat["team"]+"/"+playerStat["player"])

    with open("output/"+str(playerStat["team"])+"/"+str(playerStat["player"])+"/"+str(summonerName)+".json", "w",encoding="utf8") as f:
        json.dump(matchData, f, ensure_ascii=False, indent=2)

    return matchData


def convertJson():
    # Python program to convert
    # JSON file to CSV
    
    # Opening JSON file and loading the data
    # into the variable data
    if(os.path.exists("output/"+playerStat["team"]+"/"+playerStat["player"]+"/"+str(summonerName)+".json") == False):
        return

    with open("output/"+playerStat["team"]+"/"+playerStat["player"]+"/"+str(summonerName)+".json",encoding='utf-8') as json_file:
        matches = json.load(json_file)


    # print((matches.keys()))
    # print(matches.items())
    # now we will open a file for writing
    data_file = open("output/"+str(playerStat["team"])+"/"+str(playerStat["player"])+"/"+str(summonerName)+".csv", 'w',newline='', encoding='utf-8')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    count = 0
    
    for emp in matches.items():
        if count == 0:
            # print('emp = ',emp[1])
            # Writing headers of CSV file
            header = emp[1].keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(emp[1].values())
    
    data_file.close()

    # with open('dingjimeinv.csv',"w",encoding='utf-8') as file:
    #     data_file = file.read()
    #     print(data_file)


with open('pro.json', 'r', encoding='utf-8') as f:
    proWithrankID = json.load(f)

cntPlayer = 0
warnInfo = "\n"
GroupC_S11 =["PSG","RNG","HLE","FNC"]
for ele in proWithrankID[cntPlayer:]:
    if (ele['team'] not in GroupC_S11):
        print("skip "+ele['team']+" "+ele['player'])
        cntPlayer+=1
        continue


    playerStat = ele
    # print(playerStat["origin"]+".op.gg")
    conn = http.client.HTTPSConnection(playerStat["origin"]+".op.gg")
    if(playerStat["ac1"]!=""):
        summonerName = playerStat["ac1"]
        print(summonerName," start")
        # print(" summonerName = ",summonerName)
        OpggID =  getOpggID(str(summonerName).replace(" ","+"))
        # print(" OpggID = ",OpggID)
        askfor20("9999999999",dict())
        convertJson()
  
    if(playerStat["ac2"]!=""):
        summonerName = playerStat["ac2"]
        print(summonerName," start")
        # print(" summonerName = ",summonerName)
        OpggID =  getOpggID(str(summonerName).replace(" ","+"))
        # print(" OpggID = ",OpggID)
        askfor20("9999999999",dict())
        convertJson()

    if(playerStat["euwac"]!=""):
        conn = http.client.HTTPSConnection("euw.op.gg")
        summonerName = playerStat["euwac"]
        print(summonerName," start")
        # print(" summonerName = ",summonerName)
        OpggID =  getOpggID(str(summonerName).replace(" ","+"))
        # print(" OpggID = ",OpggID)
        askfor20("9999999999",dict())
        convertJson()


    # check if file being fetch succed

    threeacList = [playerStat["ac1"],playerStat["ac2"],playerStat["euwac"]]
    for account in threeacList:
        # print(account)
        if(account  and os.path.exists("output/"+str(playerStat["team"])+"/"+str(playerStat["player"])+"/"+str(account)+".csv") == False):
            warnInfo = playerStat["player"]+"\t"+warnInfo+"\n"+account+" failed"
    
    with open("processInedx.txt","w",encoding='utf-8') as f:
        f.write("finsh the "+str(cntPlayer)+warnInfo)
    cntPlayer+=1






