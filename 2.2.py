import csv
import matplotlib.pyplot as plt
import numpy as np

h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    dnum = {}
    ddenom = {}
    
    for i in data:
        code = i['Country Code']
        rating = i['Aggregate rating']
        votes = i['Votes']
        locality = i['Locality']
        if code == '1':
            ddenom[locality] = ddenom.get(locality, 0) + int(votes)
            x = (float(votes))*(float(rating))
            dnum[locality] = dnum.get(locality, 0.0) + x

    d = {}
    for i in dnum:
        if ddenom[i] == 0:
            wrr = 0
        else:
            wrr = dnum[i]/ddenom[i]
        d[i] = d.get(i, wrr)

    count = 0;
    print('Top 10 localities with more weighted restaurants: ')
    for i in sorted(d.items(), key = lambda item:item[1], reverse = True):
        print(i[0], '%.2f'%i[1])
        count+=1
        if count == 10:
            break
