import pandas as pd
import sys
import os
import json

with open('proWithrankID.json', 'r', encoding='utf-8') as f:
    proWithrankID = json.load(f)

allcsv = {}
fuck = "fuck"

for player in proWithrankID[:]:
    tmpCsv=os.listdir(r'./output/'+player['team']+'/'+player['player']) 
    csvAc=[]
    for ele in tmpCsv:
        if (os.path.splitext(ele)[1] == '.csv'):
            # print(ele)
            csvAc.append('./output/'+player['team']+'/'+player['player']+"/"+ele)

    # print(player['player'],csvAc)
    # print(player['team'] in allcsv )
    if((player['team'] in allcsv) == False):
        # print('create team : ',player['team'])
        allcsv[player['team']] = {}
    
    allcsv[player['team']][player['player']] = (csvAc)


# print(allcsv)
with open("foo.json", "w",encoding="utf8") as f:
    json.dump(allcsv, f, ensure_ascii=False, indent=2)



for team in allcsv:
    writer = pd.ExcelWriter(team+'.xlsx') # Arbitrary output name
    for player in allcsv[team]:
        # print( allcsv[team][player])
        for csvfile in allcsv[team][player]:
            df = pd.read_csv(csvfile)
            df.to_excel(writer,sheet_name=player+"_"+os.path.splitext(os.path.basename(csvfile))[0])
    writer.save()



# writer = pd.ExcelWriter('default.xlsx') # Arbitrary output name
# for csvfilename in os.path.join():
#     df = pd.read_csv(csvfilename)
#     df.to_excel(writer,sheet_name=os.path.splitext(csvfilename)[0])
# writer.save()



# file_list=os.listdir(r"./")
# print(file_list)

# writer = pd.ExcelWriter('default.xlsx') # Arbitrary output name
# for csvfilename in sys.argv[1:]:
#     df = pd.read_csv(csvfilename)
#     df.to_excel(writer,sheet_name=os.path.splitext(csvfilename)[0])
# writer.save()