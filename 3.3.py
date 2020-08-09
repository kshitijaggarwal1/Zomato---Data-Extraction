import csv
import matplotlib.pyplot as plt

h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    name = []
    votes = []
    d = {}
    
    for i in data:
        if i['Country Code'] == '1':
            n = i['Restaurant Name']
            v = int(i['Votes'])
            d[n] = d.get(n, 0)
            if d[n] == 0:
                d[n] = v
            else:
                if d[n] < v:
                    d[n] = v
    count = 0
    for i in sorted(d.items(), key = lambda item: item[1], reverse = True):
        name.append(i[0])
        votes.append(i[1])
        count+=1
        if count == 10:
            break

    plt.bar(name, votes)
    plt.xlabel('Name of Restaurant')
    plt.ylabel('Number of Votes')
    plt.title('Top 10 restaurants with highest number of votes')
    plt.xticks(rotation = 90)
    plt.show()
