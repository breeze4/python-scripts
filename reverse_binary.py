#http://www.reddit.com/r/dailyprogrammer/comments/vbr0z/6202012_challenge_67_easy/

def reverse_binary(n):
	binary_string = bin(n)[2:]
	full_string = ('0' * (32-len(binary_string)) + binary_string)
	return int(full_string[::-1],2)
