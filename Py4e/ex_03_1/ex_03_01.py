hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour = input("Enter Rate Per Hour:")
rph = float(rate_per_hour)
rph_greater_40 = 1.5*rph
gross_pay = 0.0
h_greater_40 = 0.0
if h > 40:
    h_greater_40 = h - 40
    gross_pay = 40*rph+h_greater_40*rph_greater_40
else:
    gross_pay = h*rph
print(gross_pay)