# tmp = '%EB%B3%91%EC%94%AC%EA%B0%99%EC%9D%80%EA%B2%8C%EC%9E%84'

# from urllib.parse import unquote

# tmp = unquote(tmp)

# print(tmp)
import pprint
import json



raw : object
with open('data.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)


# print(raw["div"]) 
# print((raw["div"][0]))

# print(len( (raw["div"][0]["div"])) )## numbers of matches


matchData : list
matchInfo = dict()
matches = raw["div"][0]["div"]

for match in matches[:]:
    # print( "gameID  :",match["div"][0]["_attributes"]["data-game-id"] )  # gameID
    matchInfo["gameID"]=match["div"][0]["_attributes"]["data-game-id"] 
    print(matchInfo)
    
#     print( "win or lose?    :",match["div"][0]["_attributes"]["data-game-result"] )  # win or lose?
#     print( "gameTime_int    :",match["div"][0]["_attributes"]["data-game-time"] )  # gameTime_int

#     print( match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"])  #GameType


#     print( match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]) ## gameTime_string

#     print( match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]) #GameLength
    
#     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][0]["img"][0]['_attributes']["alt"])#D_SummonerSpell
#     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][1]["img"][0]['_attributes']["alt"])#F_SummonerSpell
#     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][0]["img"][0]["_attributes"]["alt"]) #main_Rune
#     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][1]["img"][0]["_attributes"]["alt"]) #second_Rune

#     print("kill :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][0]["_value"] )#kill
#     print("Death :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][1]["_value"] )#Death
#     print("Assist :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][2]["_value"] )#Assist

#     print("KDARatio :",match["div"][0]["div"][0]["div"][2]["div"][1]["span"][0]["_value"])
#     if(len( match["div"][0]["div"][0]["div"][2]["div"]) >2):
#         print("Badge1 :", match["div"][0]["div"][0]["div"][2]["div"][2]["span"][0]["_value"] )
#     if(len( match["div"][0]["div"][0]["div"][2]["div"]) >3):
#         print("Badge2 :",match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"])


#     print(match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]) #champion
#     print(match["div"][0]["div"][0]["div"][3]["div"][0]["_value"])#level
#     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"])#detail cs info
#     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]) #cs and avg_cs_per_mins
#     print(match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]) #Kill Participation
#     if(len(match["div"][0]["div"][0]["div"][3]["div"]) > 3 ):
#         print(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]) #Tier Average


#     print(list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][5].keys() )[1]) #identiy if the item is exist or not

#     for target in range(7):
#         if(  list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target].keys() )[1] == 'img'):
#             print(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"])        


#     if(len(match["div"][0]["div"][0]["div"][4]["div"] )> 1):
#         print(match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]) #Control Ward
#     for teammate in range(5):
#         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]) #teammate1 champion
#         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"])#teammate1 id
    
#     for enermy in range(5):
#         print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]) 
#         print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"])






# # for match in matches[:]:
#     print( "gameID  :",match["div"][0]["_attributes"]["data-game-id"] )  # gameID


#     print( "win or lose?    :",match["div"][0]["_attributes"]["data-game-result"] )  # win or lose?
#     print( "gameTime_int    :",match["div"][0]["_attributes"]["data-game-time"] )  # gameTime_int

#     print( match["div"][0]["div"][0]["div"][0]["div"][0]["_attributes"]["title"])  #GameType


#     print( match["div"][0]["div"][0]["div"][0]["div"][1]["span"][0]["_value"][-19:]) ## gameTime_string

#     print( match["div"][0]["div"][0]["div"][0]["div"][4]["_value"]) #GameLength
    
#     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][0]["img"][0]['_attributes']["alt"])#D_SummonerSpell
#     print( match["div"][0]["div"][0]["div"][1]['div'][1]["div"][1]["img"][0]['_attributes']["alt"])#F_SummonerSpell
#     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][0]["img"][0]["_attributes"]["alt"]) #main_Rune
#     print(match["div"][0]["div"][0]["div"][1]["div"][2]["div"][1]["img"][0]["_attributes"]["alt"]) #second_Rune

#     print("kill :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][0]["_value"] )#kill
#     print("Death :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][1]["_value"] )#Death
#     print("Assist :",match["div"][0]["div"][0]["div"][2]["div"][0]["span"][2]["_value"] )#Assist

#     print("KDARatio :",match["div"][0]["div"][0]["div"][2]["div"][1]["span"][0]["_value"])
#     if(len( match["div"][0]["div"][0]["div"][2]["div"]) >2):
#         print("Badge1 :", match["div"][0]["div"][0]["div"][2]["div"][2]["span"][0]["_value"] )
#     if(len( match["div"][0]["div"][0]["div"][2]["div"]) >3):
#         print("Badge2 :",match["div"][0]["div"][0]["div"][2]["div"][3]["span"][0]["_value"])


#     print(match["div"][0]["div"][0]["div"][1]["div"][3]["a"][0]["_value"]) #champion
#     print(match["div"][0]["div"][0]["div"][3]["div"][0]["_value"])#level
#     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_attributes"]["title"])#detail cs info
#     print(match["div"][0]["div"][0]["div"][3]["div"][1]["span"][0]["_value"]) #cs and avg_cs_per_mins
#     print(match["div"][0]["div"][0]["div"][3]["div"][2]["_value"]) #Kill Participation
#     if(len(match["div"][0]["div"][0]["div"][3]["div"]) > 3 ):
#         print(match["div"][0]["div"][0]["div"][3]["div"][3]["b"][0]["_value"]) #Tier Average


#     print(list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][5].keys() )[1]) #identiy if the item is exist or not

#     for target in range(7):
#         if(  list(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target].keys() )[1] == 'img'):
#             print(match["div"][0]["div"][0]["div"][4]["div"][0]["div"][target]["img"][0]["_attributes"]["alt"])        


#     if(len(match["div"][0]["div"][0]["div"][4]["div"] )> 1):
#         print(match["div"][0]["div"][0]["div"][4]["div"][1]["span"][0]["_value"]) #Control Ward
#     for teammate in range(5):
#         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][0]["div"][0]["_attributes"]["title"]) #teammate1 champion
#         print(match["div"][0]["div"][0]["div"][5]["div"][0]["div"][teammate]["div"][1]["a"][0]["_attributes"]["href"])#teammate1 id
    
#     for enermy in range(5):
#         print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][0]["div"][0]["_attributes"]["title"]) 
#         print(match["div"][0]["div"][0]["div"][5]["div"][1]["div"][enermy]["div"][1]["a"][0]["_attributes"]["href"])