import csv
import matplotlib.pyplot as plt
h = {'user-key' : '415da0131dd99fe9349d313a3324a955', 'Accept' : 'application/json'}
with open("C:\\Users\\KSHITIJ AGGARWAL\\Desktop\\CN PDFs\\ML DS content\\zomato.csv", encoding = "latin1") as obj:
    data = csv.DictReader(obj, skipinitialspace = True)
    
    l1 = []
    l2 = []
    for i in data:
        if i['Country Code'] == '1':
            l = []
            l = list(i['Cuisines'].split(', '))
            rating = i['Aggregate rating']
            if len(l) > 1:
                continue
            l1.append(l)
            l2.append(rating)

    number_of_cuisines = []
    rating = []
    for i in range(50):
        number_of_cuisines.append(len(l1[i]))
        rating.append(l2[i])
    rating, number_of_cuisines = (list(t) for t in zip(*sorted(zip(rating, number_of_cuisines))))
    plt.plot(number_of_cuisines, rating)
    plt.xlabel('number of cuisines')
    plt.ylabel('Rating')
    plt.title('Number of Cuisines vs rating')
    plt.show()
    
