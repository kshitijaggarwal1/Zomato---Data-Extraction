import csv
import matplotlib.pyplot as plt
import numpy as np

h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    dnum = {}
    ddenom = {}
    dcount = {}
    total_votes = 0
    for i in data:
        code = i['Country Code']
        rating = i['Aggregate rating']
        votes = i['Votes']
        city = i['City']
        if code == '1':
            ddenom[city] = ddenom.get(city, 0) + int(votes)
            x = (float(votes))*(float(rating))
            dnum[city] = dnum.get(city, 0.0) + x
            dcount[city] = dcount.get(city, 0) + 1

    name = []
    value = []
    count = []
    for i in dcount:
        count.append(dcount[i])
        name.append(i)
        wrr = dnum[i]/ddenom[i]
        value.append(wrr)

    names = np.array(name)
    values = np.array(value)
    counts = np.array(count)
    values1 = np.arange(len(names))
    plt.scatter(names, counts, s = values, c = values1, edgecolors = 'black', marker = 'o')
    plt.grid()
    plt.xticks(rotation = 90)
    plt.xlabel('City')
    plt.ylabel('number of Restaurants')
    plt.show()

