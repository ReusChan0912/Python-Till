# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:31:28 2018

@author: LMI3D
"""

k = []
m = []
result = []
maxV = 10000
for i in range(10,maxV):
    m.append(i)

for num in range(10,maxV):
    for i in range(2,num):
        if num % i == 0:
           j = num / i
           print('%d = %d * %d') %(num,i,j)
           k.append(num)
           break

for i in m :
    if not i in k:
        result.append(i)
        
print(result)