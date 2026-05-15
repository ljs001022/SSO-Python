#조건문 ( if )
a = 1
b = 2
if a<b:
    s = '{}가 {}보다 작다'
    print(s.format(a, b))
    #print("1")
print()

if a>b:
    print('A')
else:
    print('B')
print()

print('A') if a>b else print('B')
print()

i = 0
if i>0:
    print('0보다 크다')
elif i<0:
    print('0보다 작다')
else:
    print('0이다')

c1 = -1
c2 = 0
c3 = 1
if c1<c2 or (c2>c3 or c1>c3):
    print('수행')
print()

if 1>0:
    pass

print('끝')