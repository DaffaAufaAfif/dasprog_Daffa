t=int(input())
win=0
while(t):
    team=list(map(int,input().split()))
    if (sum(team)>=2):
        win+=1
    t-=1
print(win)