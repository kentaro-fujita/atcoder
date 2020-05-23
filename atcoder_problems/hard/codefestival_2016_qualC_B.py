k, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
pre_index = 10**5
for i in range(k):
    max_value = 0
    max_index = 0
    for j in range(len(a)):
        if a[j] > max_value:
            max_value = a[j]
            max_index = j
    
    if pre_index != max_index:
        a[max_index] -= 1
        pre_index = max_index
    else:
        second_max_value = 0
        second_max_index = 0
        for j in range(len(a)):
            if j != max_index and a[j] > second_max_value:
                second_max_value = a[j]
                second_max_index = j
        if second_max_value == 0:
            a[max_index] -= 1
            pre_index = max_index
            ans += 1
        else:
            a[second_max_index] -= 1
            pre_index = second_max_index

print(ans)
