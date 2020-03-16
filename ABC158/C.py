def main():
    A, B = map(int, input().split(' '))

    low = int(B /0.1)
    up = int((A+1) / 0.08)
    
    value = -1
    for i in range(low,up):
        if int(i*0.08)==A and int(i*0.1)==B:
            value = i
            break
    
    print(value)

if __name__ == '__main__':
    main()