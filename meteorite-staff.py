import csv
data = []
with open('meteorite-staff.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

x=[]
y=[]
for row in data[1:]:
    x.append(int(row[0]))
    y.append(int(row[1]))

y_max = max(y)
z = [i/y_max for i in y]

import matplotlib.pyplot as plt
plt.plot(x,z)
plt.show()
