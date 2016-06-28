age = input("type in an age\n")
baby_cnt = toddler_cnt = preschooler_cnt = other_cnt = 0

if age<2:
	print 'Baby'
	baby_cnt +=1

elif age == 2 or age == 3:
	print 'Toddler'
	toddler_cnt +=1

elif age >= 4 and age < 6:
	print 'Preschooler'
	preschooler_cnt +=1

else:
	print 'Other'
	other_cnt +=1
