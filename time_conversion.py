hour12 = input().split(':')
pm_am = hour12[2][-2:] # Getting AM/PM
hour12[2] = hour12[2][:-2] # Removing AM/PM from secondes
if pm_am == 'PM':
	if hour12[0] != '12':
		hour12[0] = str(int(hour12[0]) + 12)
else:
	if hour12[0] == '12': hour12[0] = '00'
hour24 = ':'.join(hour12)
print(hour24)