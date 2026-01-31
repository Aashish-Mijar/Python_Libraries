"""
Vertically 
horizontally

vstack() row-wise-->vertically
hstack() column-wise--> horizontally
"""

import numpy as np

arr1 = np.array([1,3,5,6])
arr2 = np.array([6,9,4,65])

print(np.vstack((arr1, arr2)))
print(np.hstack(((arr1, arr2))))