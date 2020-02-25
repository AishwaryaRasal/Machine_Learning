# -*- coding: utf-8 -*-
#import random
import sys
import random
import math
#import numpy as np

### read data and labels from file

all_data=open(sys.argv[1], 'r')
trainlabels_data=open(sys.argv[2], 'r')

data=[]
train_label=[]

for line in all_data:
    row=[float(num)for num in line.split()]
    data.append(row)
    train_label.append(0)
    
#assign labels
for line in trainlabels_data:
    t=[float(num) for num in line.split()]
    train_label[int(t[1])]=t[0]

rows=len(data)
cols=len(data[0])

###Append dummy row of 1's to prevent 0 mean and variance ###
dummyrow = []

for i in range(0,cols,1):
  dummyrow.append(1)
  

#-------------------------------#
##compute Y mean
sum=0
for i in range(0,len(train_label),1):
    sum=sum+train_label[i]
ymean=sum/len(train_label)
#print("ysum: ", sum)
#print("ymean: ", ymean)

maxlen = len(max(data, key = len))
#print("maxlen: ", maxlen)
for l in data:
    if len(l) < maxlen:
        numzero = maxlen - len(l)
        l.append(numzero * 0.00001)
#print("data: ", data)
        
Xsum=[]
Xmean=[]
extra_num=0
for i in range(0, maxlen, 1):
    n=0
    col_sum = 0
    for innerlist in data:
        n+=1
        if innerlist[i] == 0.00001:
            extra_num +=1
            continue
        col_sum += innerlist[i]
    Xsum.append(col_sum)
    Xmean.append(col_sum / (n - extra_num))
#print("Xsum: ", Xsum)
#print("Xmean: ", Xmean)

##-------------compute r---------------------
r=[]
numerator=[]
den1=[]
den2=[]
den=[]
r_values = {}

for i in range(0, cols, 1):
    r.append(0)
    numerator.append(0)
    den1.append(0)
    den2.append(0)
    den.append(0.00000001)
    
for i in range(0,cols,1):
    for j in range(0,rows,1):
        if data[j][i] == 0.00001:
            continue
        numerator[i]+=(data[j][i]-Xmean[i])*(train_label[j]-ymean)
        den1[i]+=(data[j][i]-Xmean[i])**2
        den2[i]+=(train_label[j]-ymean)**2
        if (den1[i] == 0 or den2[i] == 0):
          den1[i] += .0000001
#        if den2[i] == 0:
          den2[i] += .0000001          
        den[i]=math.sqrt(den1[i]*den2[i])
#        if den[i] == 0:
#          den[i] = .0000001
    r[i]=numerator[i]/den[i]
    r_values[r[i]] = i

#----------------------choose top K----------------------
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] < lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

bubble_sort(r)
#print("sort r: ", r)

#choose top features, number=k
K = int(sys.argv[3])
#print(K)
feature=[]
topFeatures = []
for i in range(0,K,1):
    feature.append(0)
    feature[i]=r[i]
#    print("Feature number ", i+1, ": Column ",r_values.get(feature[i]))
    topFeatures.append(r_values.get(feature[i]))
#print("top k features: ", feature)

data2 = []
index = -1
a = []
for i in range(0,rows,1):
    a = []
    for j in range(0,len(topFeatures),1):
#        print("Column to keep: ", topFeatures[j])
        a.append(data[i][topFeatures[j]])
    data2.append(a)

for i in data2:
    for j in i:
        print(j, "", end = '')
    print()

