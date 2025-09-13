t=int(input())
while(t):
    word=input()
    wCount=len(word)
    if (wCount>10):
        print(word[0],(wCount-2),word[wCount-1],sep="")
    else:
        print(word)
    t-=1
