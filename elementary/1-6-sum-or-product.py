n = int(input("Enter n for me, will ya? Pretty please :)\n"))
choice = int(input("Enter 1 to obtain the sum and 2 to obtain the product of all the number from 1 to n\n"))

if(choice == 1):
	result = 0
	for i in range(1, n+1):
		result = result + i
	print("The sum of the numbers from 1 to", n, "is", result)

elif(choice == 2):
	result = 1
	for i in range(1, n+1):
		result = result * i
	print("The product of the numbers from 1 to", n, "is", result)

else:
	print("Whoops! Looks like you entered something weird. Try again?")
