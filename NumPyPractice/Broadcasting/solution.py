import numpy as np

prices = np.array([100, 300, 400, 500])
discount = 10  # scalar single value

final_prices = prices - (prices * discount / 100)

print(final_prices)

# broadcasting expands smaller to longer to match