import csv
data = []
with open('lvl.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

x=[]
y=[]
for row in data[1:-1]:
    x.append(int(row[0]))
    y.append(int(row[1].replace(',', '')))


index = 2.872

import matplotlib.pyplot as plt
# plt.yscale('function', functions =  (
#     lambda x: x**(1/index),
#     lambda x: x**(index)
# ))
plt.ylim(0.01, max(y))
plt.plot(x,y)

plt.show()
