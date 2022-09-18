import csv 
import json
import re

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            # if row['Land'] != "":

         
            # print ('True' if row.get('Lane') else 'False')
            # The most Pythonic way of checking if a value in a dictionary is defined/has zero length
            # https://stackoverflow.com/questions/7771318/the-most-pythonic-way-of-checking-if-a-value-in-a-dictionary-is-defined-has-zero

            if( True if row.get('position') else False):
                jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=2, ensure_ascii=False)
        jsonf.write(jsonString)
          
csvFilePath = r'Rank - Player2.csv'
jsonFilePath = r'pro.json'

openFile = open(csvFilePath, "r",encoding='utf-8')
readFile = openFile.read()
openFile.close()

# readFile = readFile.replace(r'Team,Lane,Player,Original area,,,EUW,,PuuID1,PuuID2,Worlds,AC1,AC2,.*,\n','Team,Lane,Player,Original area,AC1,AC2,AC3,EUW,PuuID1,PuuID2,Worlds')
readFile = re.sub(r'Team.*','team,position,player,origin,ac1,ac2,euwac,tier,PuuID1,PuuID2,Worlds',readFile,re.M |re.I)

# print(readFile)

with open(csvFilePath,"w" ,encoding='utf-8') as f: 
    f.write(readFile)


csv_to_json(csvFilePath, jsonFilePath)




openFile = open('pro.json', "r",encoding='utf-8')
readFile = openFile.read()
openFile.close()

# readFile = readFile.replace(r'Team,Lane,Player,Original area,,,EUW,,PuuID1,PuuID2,Worlds,AC1,AC2,.*,\n','Team,Lane,Player,Original area,AC1,AC2,AC3,EUW,PuuID1,PuuID2,Worlds')
readFile = readFile.replace('"origin": "KR"','"origin": "www"')
print(readFile)

with open('pro.json',"w" ,encoding='utf-8') as f: 
    f.write(readFile)