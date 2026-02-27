import numpy as np
import time

# Python time
list_data = list(range(1000000))
start = time.time()
list_result = [x * 2 for x in list_data]
print("List Time: ", time.time() - start)


#  Numpy array
array_data = np.arange(1000000)
start = time.time()
start = time.time()
array_result = array_data * 2
print("Numpy Time: ", time.time() - start)