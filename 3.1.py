import csv
import matplotlib.pyplot as plt
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    d = {}
    
    for i in data:
        if i['Country Code'] == '1':
            res = i["Restaurant Name"]
            d[res] = d.get(res, 0) + 1
    count = 0
    name = []
    qty = []
    for i in sorted(d.items(), key = lambda item: item[1], reverse = True):
        name.append(i[0])
        qty.append(i[1])
        count+=1
        if count == 15:
            break
    plt.bar(name, qty)
    plt.xticks(rotation = 90)
    plt.xlabel('Name of restaurant')
    plt.ylabel('Numberr of outlets')
    plt.title('Top 15 restaurants with maximum outlets')
    plt.show()
