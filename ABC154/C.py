def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    is_break = False
    seen = set()
    for a in A:
        if a not in seen:
            seen.add(a)
        else:
            is_break = True
            break
    
    if is_break:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()