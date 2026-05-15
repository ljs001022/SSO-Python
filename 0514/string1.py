#문자열
a = '안녕 방가워 파이썬'
print(a[0]) #안
print(a[-1]) #썬
print()

print(a[0:2]) #안녕
print()

print(a[-3:]) #파이썬
print(a[7:]) #파이썬
print()

print(len(a)) #10
print()

b = '       안녕 방가워 파이썬    '
print(len(b)) #21
print(len(b.strip())) #10
print()

c = 'Good morning'
print(c.lower())
print(c.upper())
print()

d = 'Wiack and Wiue' #Wi -> Bl
print(d.replace('Wi', 'Bl'))
print()

print(d) #str불변성

e = 'Wi' not in d
print(e)