message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]


def reverse(message):
    left_index  = 0
    right_index = len(message) - 1

    while left_index < right_index:
        # Swap characters
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1

def reverse_words(message):
	left_index = 0
	right_index = 0
	i = 0
	while message[i] != " " and i < len(message) -1:
		print(message[i])
		right_index = right_index + 1
		i = i + 1
		while left_index < right_index:
			# Swap characters
			message[left_index], message[right_index] = message[right_index], message[left_index]
			# Move towards middle
			left_index  += 1
			right_index -= 1


reverse(message)
print(message)
reverse_words(message)
print(message)

# Prints: 'steal pound cake'
print(''.join(message))