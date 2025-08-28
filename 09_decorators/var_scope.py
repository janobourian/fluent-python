from dis import dis

b = 6

def f1(a):
    print(a)
    print(b)
    b = 9

dis(f1)
f1(3)