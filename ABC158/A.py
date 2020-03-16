def main():
    S = input()
    if 'AB' in S:  
        print("Yes")
    elif 'BA' in S:
        print("Yes")
    else:
        print("No")
        

if __name__ == '__main__':
    main()

"""
A,B = map(int, input().split(' '))
N = list(map(int, inputs().split(' ')))
"""