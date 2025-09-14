#TP
#Diminta mengenkripsi pesan
#Pesan hanya alphabet dan case sensitif
def convert(pindah, karakter):
    listOfChar=["a","b","c","d","e",
                "f","g","h","i","j",
                "k","l","m","n","o",
                "p","q","r","s","t",
                "u","v","w","x","y",
                "z"]
    newChar=-1
    outTs=karakter
    for i in range(26):
        if karakter == listOfChar[i]:
            newChar = i
    if newChar!=-1:
        outTs=listOfChar[(newChar+pindah)%26]
    return outTs

t = int(input())
while(t):
    pindah = int(input())
    kalimat = input()
    myKalimat=""
    for i in kalimat:
        besar=True if i.isupper() else False
        temp=convert(pindah,i.lower())
        if besar:
            temp=temp.upper() 
        myKalimat+= temp
    print(myKalimat)
    t-=1