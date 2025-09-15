import math
n = int(input())
if n<8:
    print("Too Small")
    exit()
mod = n%3
if mod == 1:
    n-=1
elif mod ==2:
    n+=1
cakeTOP = math.ceil((n-3)/2)
topWid=cakeTOP
if cakeTOP%2==0:
    topWid+=1
cakeBOT= n-3-cakeTOP
botWid = n
if n%4>=2:
    botWid+=4-(n%4)
elif n%4==1:
    botWid-=1
blankSec = int((botWid+2)/4)
blankFir = blankSec+int(topWid/2)
print(" "*(blankFir+1),"*",sep="")
for i in range(3):
    print(" "*(blankFir),"|",sep="",end="")
    print("-|")
print(" "*(blankSec),"-"*(topWid+2),sep="")    
for i in range(cakeTOP):
    print(" "*(blankSec),"|",sep="",end="")
    print("="*(topWid),"|",sep="")
print("-"*(botWid+2))
for i in range(cakeBOT):
    print("|",sep="",end="")
    print("="*(botWid),"|",sep="")    
print("-"*(botWid+2))
