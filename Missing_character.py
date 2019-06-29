#Python
str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
list1 = [k for k in str1]
mr = int(input())
for i in range(mr):
    mass = int(input())
    check = input()
    check1 = []
    for i in check:
        for j in range(len(list1)):
            if i == list1[j]:
                check1.append(j)
    fin = 0
    check1.reverse()
    for r in range(0, len(check1)):
        if r == 0:
            x = check1[r] + check1[r]
            num = x // 64
            rem = x % 64
            tot = num + rem
            fin = fin + tot
        elif r%2 == 0:
            x = check1[r] + check1[r]
            num = x // 64
            rem = x % 64
            tot = num + rem
            fin = fin + tot
        else:
            fin = fin + int(check1[r])
    num1 = fin //64
    rem1 = fin % 64
    if fin == 0:
        print('A')
    else:
        print(list1[64-rem1])
