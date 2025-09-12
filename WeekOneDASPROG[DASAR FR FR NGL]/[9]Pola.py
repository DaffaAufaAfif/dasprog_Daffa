x= int(input())
gambar=['*','#']
for i in range(x,0,-1):
    print(gambar[i%2],end="")
    