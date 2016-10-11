# Although I'm still solving elementary problems, I strongly feel that writing a function will make sense for such a problem :)

def table(num):
	for i in range(1, 11):
		ans = i * num
		print(num, "x", i, "=", ans)

# let's loop through the function calls as well :)

for i in range(1, 13):
	table(i)