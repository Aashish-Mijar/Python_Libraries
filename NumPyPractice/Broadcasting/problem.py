prices = [200, 500, 600]
discount = 10  # 10% percent
final_prices = []

for price in prices:
    final_price = price -(price * discount / 100)
    final_prices.append(final_price)

print(final_prices)