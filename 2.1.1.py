import csv
import matplotlib.pyplot as plt
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    
    l1 = []
    l2 = []
    for i in data:
        if i['Country Code'] == '1':
            votes = i['Votes']
            rating = i['Aggregate rating']
            l1.append(votes)
            l2.append(rating)
    
    
    ratings = []
    vote = []
    for i in range(0, 10):
        ratings.append(l2[i])
        vote.append(l1[i])
    
    plt.bar(ratings, vote)
    plt.xlabel('Rating')
    plt.ylabel('Votes')
    plt.title('Rating vs votes')
    plt.show()
