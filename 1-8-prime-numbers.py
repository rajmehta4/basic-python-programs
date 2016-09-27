n = int(input("Let's just stick to the tradition: enter the value of n please!\n"))

print("The list of prime numbers from 2 to", n, "is:")
for num in range(2, n+1):
	flag = False
	iterator = num - 1
	while(iterator > 1):
		if(num%iterator == 0):	#The number is divisible by some other number! Not prime! 
			flag = True
			break				#no point in continuing now, that we know the given number is not prime
		iterator -= 1

	if(flag == False):			#if true, it means that the given number wasn't divisible by any other number. Hence, prime!
		print(num)