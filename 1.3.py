import csv
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
    key3 = []
    value3 = []

    for i in sorted(dncr.items(), key = lambda item: item[1], reverse = True):
        key1.append(i[0])
        value1.append(i[1])
    for i in sorted(dindia.items(), key = lambda item: item[1], reverse=True):
        key2.append(i[0])
        value2.append(i[1])
    for i in sorted(dcombined.items(), key = lambda item: item[1], reverse = True):
        key3.append(i[0])
        value3.append(i[1])
        
    for i in sorted(dncr.items(), key = lambda item: item[1], reverse = True):
        key1.append(i[0])
        value1.append(i[1])
    for i in sorted(dindia.items(), key = lambda item: item[1], reverse=True):
        key2.append(i[0])
        value2.append(i[1])

    print('Top 10 cuisines served in Delhi NCR : ')
    for i in range(0, 10):
        print(key1[i], value1[i])
    print('')
    print('Top 10 cuisines served in Rest of India : ')
    for i in range(0, 10):
        print(key2[i], value2[i])
    print('')
    print('Top 10 cuisines served in Delhi NCR along with Rest of India : ')
    for i in range(0, 10):
        print(key3[i], value3[i])
