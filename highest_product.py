list_of_ints = [1, 6, 7, 7, 9, 12, 1, 0, 2, 23, 4, 4, 44, 44, -1, 42, 1543, 1]

def highest_product(list_of_ints):
	highest_list = [0] * 2
	lowest_list = [0] * 2
	max_product = 0
	for i in list_of_ints:
		min_highest = min(highest_list)
		max_lowest = max(lowest_list)
		if i > min_highest:
			highest_list[highest_list.index(min_highest)] = i
		if i < max_lowest:
			lowest_list[lowest_list.index(max_lowest)] = i

	for i in list_of_ints:
		new_high = i * (highest_list[0] * highest_list[1])
		new_low = i * (lowest_list[0] * lowest_list[1])
		if new_high > max_product:
			max_product = new_high
		if new_low > max_product:
			max_product = new_high
	return max_product




print(highest_product(list_of_ints))