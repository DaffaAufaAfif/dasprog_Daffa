#Tower Level Evalation
n,e,k = map(int, input().split())
a = list(map(int, input().split()))
for loop in range(k):
    l,r = map(int, input().split())
    for i in range(l,r):
       e-=a[i-1]
if e < 0:
    print(f"NT, kurang {abs(e)} energi sih.")
else:
    print(f"EZ banget, energiku sisa {e}!")