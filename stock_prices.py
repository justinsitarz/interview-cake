stock_prices = [10, 7, 5, 3, 1]

def get_max_profit(stock_prices):
	if len(stock_prices) < 2:
		raise ValueError('Getting a profit requires at least 2 prices')
	min_price = stock_prices[0]
	max_profit = stock_prices[1] - stock_prices[0]
	for i in range(1, len(stock_prices)):
		if stock_prices[i] - min_price > max_profit:
			max_profit = stock_prices[i] - min_price
		elif stock_prices[i] < min_price:
			min_price = stock_prices[i]

	return max_profit


print(get_max_profit(stock_prices))
