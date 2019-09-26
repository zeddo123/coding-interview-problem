def multiple5(grade):
	if grade < 100:
		tenths = grade // 10 * 10
		units = grade % 10
		if units <= 5:
			return tenths + 5
		else:
			return tenths + 10
	return 100

def rounding_grades(grade):
	if grade >= 38:
		mult5 = multiple5(grade)
		if mult5 - grade < 3:
			return mult5
	return grade

number_sdnt = int(input())
rounded_grades = []

for i in range(number_sdnt):
	rounded_grades.append(rounding_grades(int(input())))

for i in rounded_grades:
	print(i)