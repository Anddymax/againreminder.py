def computepay(hours,rate):
    if h>40:
        g=h*r
        q=(h-40)*(0.5*r)
        p=g+q
        return p
    else:
        p=h*r
        return p
hours = input("Enter Hours:")
rate = input("Enter Rate:")
h = float (hours)
r = float (rate)
pay = computepay(h,r)
print("Pay",pay)    
    
