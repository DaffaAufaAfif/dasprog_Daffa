n = int(input())
dictAv={}
for i in range(n):
    name, val = map(lambda x: int(x) if x.isdigit() else x,input().split())
    dictAv.update({name:val})
c = int(input())
prTs=[]
for i in range(c):
    name, val = map(lambda x: int(x) if x.isdigit() else x,input().split())
    dictAv.update({name:(dictAv.get(name)-val)})
    prTs.append(name)
print("CHARLIE")
for i in prTs:
    print(i,end=" ")
print("\nSTORAGE")    
for i in dictAv:
    print(i,": ",dictAv.get(i),sep="")