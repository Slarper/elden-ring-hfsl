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


# def mean(x):
#     r = 0
#     l = len(x)
#     for i in x:
#         r += i/l
#     return r

def inner_product(x,y):
    if not len(x) == len(y):
        raise ValueError('not len(x) == len(y)')
    
    r = 0
    for i in range(len(x)):
        r += x[i]*y[i]

    return r

def module_square(x):
    r = 0
    for i in x:
        r += i**2

    return r

def module(x):
    return module_square(x)**0.5

from statistics import mean
def linearity(x,y):
    x_mean = mean(x)
    y_mean = mean(y)
    x1 = [i-x_mean for i in x]
    y1 = [i-y_mean for i in y]
    return inner_product(x1,y1)/(module(x1)*module(y1))

import scipy.stats as ss
def linearity_index(x,y,index):
    z = [i**(1/index) for i in y]
    return ss.pearsonr(x, z).statistic

def linspace(start, stop, sample=50):
    r = []
    step = (stop-start)/sample
    for i in range(sample):
        r.append(start+i*step)
    return r

import numpy as np
x20 = x[20:]
y20 = y[20:]



z = linspace(0.1,10)
w = [linearity_index(x20,y20,i) for i in z]

def find_max(l):
    index = 0
    m = l[0]
    for i in range(len(l)):
        if l[i] > m:
            m=l[i]
            index = i
    return index
print(w[find_max(w)])
print(z[find_max(w)])

import matplotlib.pyplot as plt
# plt.ylim(0.01, max(y))
plt.plot(z,w)

plt.show()
