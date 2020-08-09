import csv
import matplotlib.pyplot as plt

h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    d = {}
    for i in data:
        l = []
        if i['Country Code'] == '216':
            l = list(i['Cuisines'].split(', '))
            for j in l:
                d[j] = d.get(j, 0) + 1

    count = 0
    name = []
    num = []
    for i in sorted(d.items(), key = lambda item:item[1], reverse = True):
        name.append(i[0])
        num.append(i[1])
        count+=1
        if count == 10:
            break

    plt.pie(num, labels = name, autopct = "%.2f")
    plt.title('Top 10 cuisines served in USA')
    plt.show()
