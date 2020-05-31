s = list(input())
n = len(s)

# if n == 1:
#     print("D")
# elif n == 2:
#     print("DP")
# else:
#     for i in range(1,n-1):
#         if s[i] == '?' and s[i+1] == 'D':
#             s[i] = 'P'
#     for i in range(n):
#         if s[i] == '?':
#             s[i] = 'D'
#     print(''.join(s))

for i in range(n):
    if s[i] == '?':
        s[i] = 'D'

print(''.join(s))
