#함수(function)

def m1():
    print('이것이 펑션')
m1()
print()

def m2(name, age):
    print('name:', name, ' age:', age)
m2('홍길동', 25)
print()

def m3(*ar):
    #print(type(ar)) #tuple
    for x in ar:
        print(x)
m3('짜장', '짬뽕')
m3('짜장', '짬뽕', 100, 200)
print()

def m4(**pa):
    #print(type(pa)) #dict
    for k, v in pa.items():
        print(k, v)
m4(name='길동', age=20, addr='서울')
print()

def m5(a, b, c):
    print('a:', a, ' b:', b, ' c:', c)
m5(c='가', b='나', a='다')
print()

def m6(param='바보'):
    print(param)
m6('천재')
m6()
print()

def m7(li):
    for x in li:
        print(x)
li = ['a', 'b', 'c']
m7(li)
print()

def m8(a, b):
    return a+b
r = m8(10, 20)
print('r:', r)

def m9():
    pass