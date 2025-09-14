#Deepened Bond
from math import sqrt
t = int(input())
while(t):
    a = int(input())
    #cari pangkat terdekat, ya 0*0 termasuk[gak dilarang]
    for i in range (4):
        a-=int(sqrt(a))**2
    if a==0:
        print("LEAVE")
    else:
        print("ERASE")
    t-=1