'''
practice Matplotlib in wikidocs.net/92071
'''
from matplotlib import pyplot as plt
import math
import numpy as np

def sq(x):
    return math.sqrt(x)

plt.plot([1, 2, 3, 4, 5, 6, 7, 8, 9], 
         [sq(1), sq(2), sq(3), sq(4), sq(5), sq(6), sq(7), sq(8), sq(9)])
plt.show()

plt.plot([1, 2, 3, 4])
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# plt.plot([1, 2, 3, 4, 5], [1.1, 2,2, 3.3, 4.4, 5.5]) # error!
# plt.show()

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()