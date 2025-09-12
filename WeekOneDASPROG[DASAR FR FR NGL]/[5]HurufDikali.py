def strConvert(a):
    b=["a","b","c","d","e",
   "f","g","h","i","j",
   "k","l","m","n","o",
   "p","q","r","s","t",
   "u","v","w","x","y",
   "z"]
    ret=0
    for i in b:
        ret+=1
        if a==i:
            return ret
    return 1 #anggep tidak ada
def isNum(a):
    b=["1","2","3","4","5","6","7","8","9","0"]
    for i in b:
        if a==i:
            return True
    return False
x=input()
x=x.lower()
hasil=1
for i in (x):
    if not isNum(i):
        conv=strConvert(i)
    else:
        conv=int(i)
    hasil*=conv
print(hasil)
#aslinya bisa pake ASCII, tapi gak berani