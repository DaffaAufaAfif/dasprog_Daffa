x =list(map(len,input().split()))
if (x[1] > x[0] and x[1]>x[2]) or (x[1] < x[0] and x[1] < x[2]):
    print("Yeehaaw")
elif (x[2]>x[1] and x[1]>x[0]) or (x[2]<x[1] and x[1]<x[0]):
    print("Woohoohoo")
elif (x[2] == x[1]) or (x[1]==x[0]) or (x[0]==x[2]):
    print("Hebwueh")
#evaluasi dari jawaban temen
#pada input bisa pakai map split tapi tipenya len agar langsung jadi panjangnya
##Udah diperbaiki.