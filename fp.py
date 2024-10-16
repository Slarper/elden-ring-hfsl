import csv
data = []
with open('fp.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

x=[]
y=[]
z = []
for row in data[3:]:
    x.append(int(row[0]))
    y.append(int(row[1].replace(',', '')))
    z.append(int(row[2].replace(',', '')))


import matplotlib.pyplot as plt

ax1 = plt.gca()
ax1.set_xlim([0,110])
ax1.set_ylim([0,max(y)*1.1])
ax1.plot(x,y)
# ax1.axvline(max(x),zorder =0, linestyle='--')
# ax1.axhline(max(y),zorder =0)

ax2 = ax1.twinx()
ax2.bar(x,z,color = "orange")
ax2.set_ylim([0,2*max(z)])

ax1.set_zorder(2.5)
ax1.set_frame_on(False)

w = [j/i for i,j in zip(y,z)]
ax3 = ax2.twinx()
# Hide the y-axis numbers (tick labels) for ax3
ax3.tick_params(axis='y', labelright=False, labelleft = False)
ax2.tick_params(axis = 'y', labelright = True, labelleft = False,right=True, left=False)
ax3.bar(x,w,color='red',alpha = 0.4)


plt.savefig('fp.png',dpi = 200)
