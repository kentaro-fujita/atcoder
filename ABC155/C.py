def main():
    N = int(input())

    count = dict()
    for i in range(N):
        s = input()
        try:
            count[s] += 1
        except:
            count[s] = 1
    
    sort_ = sorted(count.items(), key=lambda x:x[1], reverse=True)

    max_value = sort_[0][1]
    item = []
    for key,value in sort_:
        if value == max_value:
            item.append(key)
        else:
            break
    
    item.sort()
    for ans in item:
        print(ans)
    
if __name__ == '__main__':
    main()

"""
A, B = input().split(' ')
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""