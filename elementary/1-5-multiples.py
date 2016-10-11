n = 17
result = 0

for i in range(1, n+1):
	if(i%3 == 0 or i%5 == 0):
		result = result + i

print("The result is:", result)
print("Note: We've assumed n to be 17 and only multiples of 3 and/or 5 have been considered for the result.")