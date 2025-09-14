#Ya ya dekripsi sangat membantu
#Cmd -> Arah pindah
#K -> besar perpindahan
#sampe end of file? klo di C++ pake while(cin>>x), izin pake while(true) mas
def enkrip(mcd,offset,char):
    listOfChar=["a","b","c","d","e",
                "f","g","h","i","j",
                "k","l","m","n","o",
                "p","q","r","s","t",
                "u","v","w","x","y",
                "z"]
    newChar=-1
    outTs=char
    for i in range(26):
        if char == listOfChar[i]:
            newChar = i
    if newChar==-1:
        return outTs
    if mcd == 1: #arahnya ke kanan
        outTs = listOfChar[(offset+newChar)%26]
    else:
        outTs = listOfChar[(newChar-offset)%26]
    return outTs
    
cMd,K = map(int,input().split())
while(True):
    try:
        tsPMO = input()
    except EOFError:
        break
    nwOut=""
    for i in tsPMO:
        bigWoi=False
        if i.isupper():
            bigWoi=True
        temp=enkrip(cMd,K,i.lower())
        if bigWoi:
            temp = temp.upper()
        nwOut+=temp
    print(nwOut)

    