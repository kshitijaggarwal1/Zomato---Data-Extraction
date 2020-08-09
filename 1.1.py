import matplotlib.pyplot as plt
import csv
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    cities = ['New Delhi', 'Noida', 'Gurgaon', 'Ghaziabad', 'Faridabad']
    totalInNCR = 0
    rem = 0
    for i in data:
        if i['City'] in cities:
            totalInNCR+=1
        elif i['Country Code'] == '1':
            rem+=1
    x = ['Delhi-NCR', 'India excluding NCR']
    y = [totalInNCR, rem]
    plt.bar(x, y)
    plt.title('Bar Graph')
    plt.xlabel('Region')
    plt.ylabel('Number of Restaurants')
    plt.show()
