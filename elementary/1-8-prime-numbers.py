n = int(input("Let's just stick to the tradition: enter the value of n please!\n"))

print("The list of prime numbers from 2 to {} is:".format(n))

for num in range(2, n+1):

	flag = False

	for iterator in range(2, num):
		if(num % iterator == 0):
			flag = True
			break

	if(flag == False):
		print(num)