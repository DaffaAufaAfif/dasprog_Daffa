#A Slight Change
n = int(input())
x = list(map(int,input().split()))
s=[0,0,0,0,0,0,0,0,0] #1-9, anggep semuanya akan kepakai aja
for i in x:
    s[i-1]+=1
print(n-max(s)) #banyak ruagan dikurangi ruangan warna s[](maksudnya warna mayoritas)