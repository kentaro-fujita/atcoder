N = input()

one = int(N[-1])

if one in [2, 4, 5, 7, 9]:
    print("hon")
elif one in [0, 1, 6, 8]:
    print("pon")
else:
    print("bon")
