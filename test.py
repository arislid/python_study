#%% 
a = 100
b = 50

res = a+b
print("res = ", res)
# %%
import numpy as np
import matplotlib.pyplot as plt

I = ([-2+2j, -1+2j, 0+2j, 1+2j, 2+2j, -1-2j, 0-2j, 1+2j])
x = [x.real for x in I]
y = [y.real for y in I]

plt.plot(x,y,'o')
plt.xlabel('real values')
plt.ylabel('imag values')
plt.title('Graph of complex number')
plt.grid(True)
plt.show()
# %%
aa = []
bb = []
value = 0

for i in range(0, 100) :
    aa.append(value)
    value += 2

for i in range(0, 100) :
    bb.append(value)
    value -= 2

print(aa[0:3])
# %%
aa1=[10, 20, 30]
bb1=[40, 50, 60]

cc = aa1+bb1
print(cc)

dd=aa1*3
print(dd)
# %%
aa = [10,20,30,40,50,60,70]
aa[1] = 200
aa = []
aa.sort()
# %%
myList = [3,10,20]
myList.append(40)
print(myList)
# %%
list1 = []
list2 = []
value =1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []