def longest_repetition(chars):
	if not chars:
		return ("", 0)
	best_l = 0
	curr_l = 0
	curr_c = chars[0]
	best_c = chars[0]
	chars = chars + " "
	for index in range(len(chars)-1):
		if chars[index]==chars[index+1]:
			curr_l+=1
			if curr_l>best_l:
				best_l = curr_l
				best_c = curr_c
		else:
			curr_l+=1
			if curr_l>best_l:
				best_l = curr_l
				best_c = curr_c
			curr_c = chars[index+1]
			curr_l = 0

	return (best_c, best_l)


print(longest_repetition('bbbaaabaaaa'))
