import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    ratings = []
    xt = np.arange(33)
    for i in data:
        if i['Country Code'] == '1':
            res = i['Aggregate rating']
            if res == '0':
                continue
            ratings.append(res)
    
    ratings.sort()
    distinct = len(Counter(ratings).keys())
    
    plt.hist(ratings, bins = distinct, edgecolor = 'black')
    plt.xticks(xt, rotation = 90)
    plt.xlabel('Aggregate Rating')
    plt.ylabel('Number of times this rating appears')
    plt.title('Ratings histogram')
    plt.show()
    
