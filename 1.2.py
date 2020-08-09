import csv
import requests
import json
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    cities = ['New Delhi', 'Noida', 'Gurgaon', 'Ghaziabad', 'Faridabad']
    india = set()
    ncr = set()
    csvAnswer = []
    count = 0
    for i in data:
        l = []
        if i['City'] in cities:
            l = list(i['Cuisines'].split(', '))
            for j in l:
                ncr.add(j)
        elif i['Country Code'] == '1':
            l = list(i['Cuisines'].split(', '))
            for j in l:
                india.add(j)
    print('Cuisines which are not present in Delhi NCR but in rest of India: ')
    for i in india:
        if i not in ncr:
            print(i)
            csvAnswer.append(i)


APIanswer = []
p = {'city_id' : '1'}
r = requests.get('https://developers.zomato.com/api/v2.1/cuisines', params = p, headers = h)
data = r.json()
for i in data['cuisines']:
    APIanswer.append(i.get('cuisine').get('cuisine_name'))
print("")
print('The cuisines from the above answer common to obtained through API: ')
for i in csvAnswer:
    if i in APIanswer:
        print(i)
print("")
print("Hence, the data is not correct due to incomplete dataset provided.")
