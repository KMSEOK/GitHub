cards = 100

for i in range(1, cards+1):
    flag = False
    for j in range(1, cards+1):
        if i%j ==0:
            flag = not flag
    if flag:
        print(i)