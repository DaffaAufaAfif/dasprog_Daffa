y,x= map(int,input().split())
loop=['*','#']
gambar = 0
for n in range(y):
    for i in range(x):
          print(loop[gambar],end="")
          gambar= (gambar+1)%2
    print(" ")