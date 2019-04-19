def computepay(hrs, rate):
	if hrs <= 40:
		gross_pay = hrs * rate
	else:
		gross_pay = 40 * rate + ( (hrs - 40) * (rate * 1.5) )

	return(gross_pay)
hrs = float(raw_input("Enter Hours: "))
rate = float(raw_input("Enter Rate per Hour: "))

print computepay(hrs,rate)
