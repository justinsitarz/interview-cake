import math


char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

def reverse_list_in_place(char_list):
	for i in range(math.floor((len(char_list)/2))):
		left = char_list[i]
		char_list[i] = char_list[-1-i]
		char_list[-1-i] = left
	return char_list

print(reverse_list_in_place(char_list))


