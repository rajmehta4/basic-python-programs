# the following code works all - positive/negative integers and positive/negative floating point numbers

import sys

inp = []

for num in input().split():

	flag = 0

	for i in num:
		if(i == '.'):
			flag = 1
			break
	try:		
		if(flag == 1):
			inp.append(float(num))
		else:
			inp.append(int(num))

	except ValueError:
		print("I asked you to enter only numbers, dumb-ass! :P")
		sys.exit()

# The above code ensures that only integers and floats are provided as input

for i in range(1, len(inp)):
	if(inp[0] < inp[i]):
		inp[0] = inp[i]

largest = inp[0]

print("The largest number in your list is {}!".format(largest))