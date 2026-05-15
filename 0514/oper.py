#연산자(Operator)

#(1) 산술 ( +, -, *, /, % , //, ** )
a = 1/2
print(a)
print('a: ' + str(a))
print('a:', a) #float
print('int(a)', int(a)) #(DownCasting) float -> int
print()

b = 1//2
print('b:', b)
print()

c = 2**3
print('c:', c)
print()

#(2) 논리 ( and, or, not )
i = 1
j = 0
d1 = True and i>j
print('d1:', d1)
d2 = True or i<j
print('d2:', d2)
d3 = not i>j
print('d3:', d3)
print()

#(3) Identity ( is, is not )
e = '김치'
f = 10
g = e is not f
print('g:', g)
print()

#(4) Membership ( in, not in )
li = ['a', 'b', 'c']
h = 'b' not in li
print('h:', h)
print()

