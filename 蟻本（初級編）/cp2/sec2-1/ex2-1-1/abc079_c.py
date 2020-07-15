s = list(input())

for i in range(1 << 3):
    form = ""
    for j in range(3):
        form += s[j]
        if i & 1 << j:
            form += "+"
        else:
            form += "-"
    form += s[-1]
    if eval(form) == 7:
        print(form + "=7")
        exit()
