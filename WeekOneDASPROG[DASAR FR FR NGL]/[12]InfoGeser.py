def geser(ix,en):
    alp=["a","b","c","d","e",
   "f","g","h","i","j",
   "k","l","m","n","o",
   "p","q","r","s","t",
   "u","v","w","x","y",
   "z"]
    offside=0
    mark=0
    for i in range(26):
        if alp[i]==ix[0]:
            mark=i
        if alp[i]==en[0]:
            offside=i
            break
    #kalo gak logis
    if (offside<mark):
        print("kena")
        return -1 #gak manuk akal

    offside-=mark
    for i in range(len(ix)):
        for j in range(26):
            if ix[i]==alp[j]:
                if (en[i]!=alp[(j+offside)%26]): #mod 26 incase ada yang kelebihan
                    return -1
    return offside
x=input()
en=input()
ix=x[::-1]#balik dulu,revers x pake slicing
res=geser(ix.lower(), en.lower())#cek jarak pergeseran
if (res==-1):
    print("Mending pulang aja")
else:
    print("Silahkan berjalan sejauh "+str(res)+" meter")