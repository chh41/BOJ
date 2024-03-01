a = int(input())

q = 25
d = 10
n = 5
p = 1
z = [0,0,0,0]
zz = 0
for i in range(a):
    x = int(input())
    z[0] = x//q
    zz = x%q
    z[1] = zz//d
    zz = zz%d
    z[2] = zz//n
    zz = zz%n
    z[3] = zz//p
    print(*z)
