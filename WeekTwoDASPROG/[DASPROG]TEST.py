#TEST: Stop taking inputs after 42
while True:
    i = int(input())
    if i  == 42:
        break
    print(i)