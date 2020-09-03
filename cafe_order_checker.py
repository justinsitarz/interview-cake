# dine_in = [1, 3, 5]
# take_out = [2, 4, 6]
# served = [1, 2, 4, 6, 5, 3]

take_out = [17, 8, 24]
dine_in = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

def cafe_order_checker(dine_in, take_out, served):
	dine_in_index = 0
	take_out_index = 0
	for s in served:
		if s == dine_in[dine_in_index]:
			dine_in_index += 1
		elif s == take_out[take_out_index]:
			take_out_index += 1
		else:
			return "Out of order"
	return 'In order'



print(cafe_order_checker(dine_in, take_out, served))



