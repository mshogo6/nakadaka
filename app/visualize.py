def visualize(input):
	list = []
	kana = []
	num = 0
	for char in input:
		if(char == '['):
			num += 1
		elif(char == ']'):
			num -= 1
		else:
			kana.append(char)
			list.append(num)
	output = ''''''
	for i in reversed(range(min(list), max(list) + 1)):
		for n, c in zip(list, kana):
			if(n == i):
				output += c
			else:
				output += '　'
		output += '\n'
	return (output, max(list) -  min(list) + 1)