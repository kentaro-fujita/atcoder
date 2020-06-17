s = input()
t = input()

if s == t:
    print('same')
elif s.lower() == t.lower():
    print('case-insensitive')
elif s != t:
    print('different')