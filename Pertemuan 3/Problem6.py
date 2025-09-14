#Array Senilai
n = int(input()) #gausah ya gpp sih, toh ini py gak perlu deklarasi awal
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = int(input())
while(t):
    l,r = map(int,input().split())
    sumA=0
    sumB=0
    for i in range (l,r+1):
        sumA+=a[i]
        sumB+=b[i]
    print("YA") if sumB == sumA else print("TIDAK")
    t-=1