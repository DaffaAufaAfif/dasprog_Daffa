#sumtrian pake dp
t=int(input())
while(t):
    tall=int(input())
    dp=[]
    for i in range(tall):
        takIt=list(map(int,input().split()))
        temp=[]
        if (i>0):
            for j in range(i+1):
                #print(dp)
                kiri = dp[i-1][j-1] if (j>0) else -1
                atas = dp[i-1][j] if (j<=i-1) else -1
                #print(i,j,kiri,atas, takIt)
                temp.append(takIt[j]+max(kiri,atas))  
        else:
            dp.append(takIt)
            continue
        #print(temp)
        dp.append(temp)
    t-=1
    print(max(max(dp)))
