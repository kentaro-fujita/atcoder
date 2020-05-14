n = int(input())

print(f'{n}:', end='')
temp = n
for i in range(2, int(n**(1/2))+1):
    if temp % i == 0:
        while temp % i == 0:
            print(f' {i}', end='')
            temp //= i

if temp != 1:
    print(f' {temp}', end='')

print('')
