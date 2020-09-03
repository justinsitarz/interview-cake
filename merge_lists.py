my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(my_list, alices_list):
	new_list = [] * (len(my_list) + len(alices_list))
	ml_count = 0
	m_len = len(my_list)
	al_count = 0
	for i in range(len(my_list) + len(alices_list)):
		if (ml_count < m_len) and (my_list[ml_count] < alices_list[al_count]):
			new_list.append(my_list[ml_count])
			ml_count += 1
		else:
			new_list.append(alices_list[al_count])
			al_count += 1
	return new_list

print(merge_lists(my_list, alices_list))