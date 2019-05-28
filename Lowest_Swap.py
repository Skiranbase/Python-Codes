t = int(input())
for x in range(t):
    num1 = int(input())
    a = list(map(int, input().split()))
    maxs = max(a)
    position = -1
    list1 = []
    val1 = []
    for i in a:
        position = position + 1
        if i == maxs:
            list1.append(position)
    if len(a)%2 == 0:
        mid2 = int(len(a)/2)
        mid1 = int((len(a)/2)-1)
        for i in list1:
            if i <= mid1:
                val = mid1-i
                val1.append(val)
            elif i >= mid2:
                val = i-mid2
                val1.append(val)
        print(min(val1))
    else:
        mid = len(a)/2
        mid = int(mid - 0.5)
        for i in list1:
            if i <= mid:
                val = mid - i
                val1.append(val)
            elif i >= mid:
                val = i-mid
                val1.append(val)
        print(min(val1))
