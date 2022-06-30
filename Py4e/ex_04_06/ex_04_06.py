hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hour = input("Enter Rate Per Hour:")
r = float(rate_per_hour)
rph_greater_40 = 1.5*r

def computepay(h, r):
    if h > 40:
        h_greater_40 = h - 40
        gross_pay = 40*r+h_greater_40*rph_greater_40
        return gross_pay
    else:
        gross_pay = h*r
        return gross_pay

p = computepay(h,r)
print("Pay", p)