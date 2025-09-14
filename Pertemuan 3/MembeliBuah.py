#implementasi 2dnya mau dipake dimana? ini 1D udah cukup
#apa maksudnya ini harusnya DP?
#sepaham saya gini
n, k = map(int, input().split())
a = list(map(int,input().split()))
yes=0
for i in a:
    if i<=k:
        yes+=1
print(yes)