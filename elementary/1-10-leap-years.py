import datetime

year = datetime.datetime.now().year

print("The next 20 leap years are:")

for i in range(1, 21):
	year += 4
	print(year)