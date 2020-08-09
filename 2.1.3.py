import csv
import matplotlib.pyplot as plt
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    
    l1 = []
    l2 = []
    for i in data:
        if i['Country Code'] == '1':
            cost = i['Average Cost for two']
            rating = i['Aggregate rating']
            l1.append(cost)
            l2.append(rating)
    
    
    ratings = []
    cost = []
    ratings, cost = (list(t) for t in zip(*sorted(zip(l2, l1))))
    for i in range(0, 10):
        ratings.append(l2[i])
        cost.append(l1[i])
    
    plt.bar(ratings, cost)
    plt.xlabel('Rating')
    plt.ylabel('Average cost')
    plt.title('Comparison between Rating and average cost')
    plt.show()
