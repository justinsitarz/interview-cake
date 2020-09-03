def permutation_palindrome(string):
	char_dict = {}
	total = 0
	for c in string:
		if c in char_dict:
			char_dict[c] += 1
		else:
			char_dict[c] = 1
	for d in char_dict:
		total += char_dict[d] % 2
	if total > 1:
		return False
	else:
		return True


print(permutation_palindrome('cccciiilll'))