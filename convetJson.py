# Python program to convert
# JSON file to CSV
 
 
import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('dingjimeinv.json',encoding='utf-8') as json_file:
    matches = json.load(json_file)


# print((matches.keys()))
# print(matches.items())
# now we will open a file for writing
data_file = open('dingjimeinv.csv', 'w',newline='', encoding='utf-8')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
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
   
