from dis import dis

b = 6


def f1(a):
    global b
    print(a)
    print(b)
    b = 9
    print(b)


f1(5)

dis(f1)
