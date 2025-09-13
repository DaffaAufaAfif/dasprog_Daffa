import math

x1, y1, r1 = map(float, input().split())
x2, y2, r2 = map(float, input().split())

# Jarak antar pusat
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Ada titik yang saling intersect
if d < r1+r2:
    a = (r1**2 - r2**2 + d**2)/(2*d)
    h = math.sqrt(r1**2 - a**2)
    xm, ym = x1 + (a*(x2-x1))/d, y1 + (a*(y2-y1))/d
    
    x3 = round(xm + (h*(y2-y1))/d, 2) # bulatkan tapi biarkan 2 koma belakang = 3.14111123 -> round(x,2) -> 3.14
    y3 = round(ym - (h*(x2-x1))/d, 2)
    x4 = round(xm - (h*(y2-y1))/d, 2)
    y4 = round(ym + (h*(x2-x1))/d, 2)
    sum = x3+x4+y3+y4
    if x3 != x4 and y3 != y4:
        print("Tidaaaaaak, airnya muncrat!")
        print(f"{sum:.2f}")
    else:
        print("Fyuh, hampir saja")
        print(f"{x3:.2f} {y3:.2f}")
else:
    print("Amang ges")