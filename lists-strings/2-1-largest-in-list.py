import sys

inp = []
flag = 0

for item in input().split():

	for i in item:
		if(i == '.'):
			flag = 1
			break
	try:		
		if(flag == 1):
			inp.append(float(item))
		else:
			inp.append(int(item))

	except ValueError:
		print("I asked you to enter only numbers, dumb-ass! :P")
		sys.exit()

# The above code ensures that only integers and floats are provided as input

for i in range(0, ):

print("The largest number in your list is {}!".format(largest))