#soal katamari
maxL=32
x=int(input())
mark=0
for i in range(maxL):
    if (x<2**i):
        mark=i
        break
jarakKri= (x-(2**(mark-1) -1))
jarakKnn= (2**(mark) -1 -x) 
if (x==0):
    jarakKri=2
    jarakKnn=1
if (min(jarakKnn,jarakKri)==0):
    print("It's the perfect amount, nice!")
elif (min(jarakKnn,jarakKri)==jarakKri):
    print(f"Maybe it's better to remove {jarakKri} fences, just to be perfect")
else:
    print(f"Maybe it's better to add {jarakKnn} fences, just to be perfect")
