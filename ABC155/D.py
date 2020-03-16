def main():
    N, K = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))

    print(max(A))
    sorted_dot = []
    while True:
        max_value = max(A)
        min_value = min(A)
        A.remove(min_value)
        second_min = min(A)
        A.append(min_value)
        if max_value*min_value > second_min*min_value:
            sorted_dot.append(second_min*min_value)
            # A.remove(second_min)
        else:
            sorted_dot.append(max_value*min_value)
        A.remove(max_value)
        if len(sorted_dot) == K:
            break
    
    print(sorted_dot)
        


if __name__ == '__main__':
    main()

"""
A, B = input().split(' ')
A, B = map(int, input().split(' '))
N = list(map(int, input().split(' ')))
"""