x= int(input())
gambar = ['#','#','*','*']
for i in range(x):
    print(gambar[i%4],end="")