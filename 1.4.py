import csv
import matplotlib.pyplot as plt
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    cities = ['New Delhi', 'Noida', 'Gurgaon', 'Ghaziabad', 'Faridabad']
    dncr = {}
    dindia = {}
    dcombined = {}
    for i in data:
        l = []
        if i['City'] in cities:
            l = list(i['Cuisines'].split(', '))
            for j in l:
                dncr[j] = dncr.get(j, 0) + 1
                dcombined[j] = dcombined.get(j, 0) + 1
        if i['Country Code'] == '1':
            l = list(i['Cuisines'].split(', '))
            for j in l:
                dindia[j] = dindia.get(j, 0) + 1
                dcombined[j] = dcombined.get(j, 0) + 1

    key1 = []
    value1 = []
    key2 = []
    value2 = []
    for i in sorted(dncr.items(), key = lambda item: item[1], reverse = True):
        key1.append(i[0])
        value1.append(i[1])
    for i in sorted(dindia.items(), key = lambda item: item[1], reverse=True):
        key2.append(i[0])
        value2.append(i[1])
    
    
    plt.plot(key1, value1, color = 'skyblue', marker = 'o')
    plt.plot(key2, value2, color = 'olive', linestyle = 'dashed')
    plt.title('Difference in the cuisines served in Delhi-NCR and rest of India')
    plt.xlabel('Cuisines')
    plt.ylabel('Demand')
    plt.xticks(rotation = 90)
    plt.legend(['Delhi-NCR', 'Rest of India'])
    plt.show()
