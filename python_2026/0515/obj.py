# class 와 object

class Human1: #빈클래스
    pass

m1 = Human1() #객체생성
print(m1)

class Human2: #멤버(속성==property)가 1개인 클래스
    name = '길동'

m2 = Human2() #객체생성
print('m2.name:', m2.name)
print()

class Human3: #클래스
    def __init__(self, name, age): #생성자
        self.name = name
        self.age = age
    def m1(self): #메소드
        print('m1()')
    def m2(self, addr): #메소드
        self.addr = addr
        print('m2() name:', self.name, ', age:', self.age, ', addr:', self.addr)


m3 = Human3('순신', 30) #객체생성
#print(type(m3)) #Human3

m3.m1() #함수(사용1)
m3.m2('성남시') #함수(사용2)
print('m3.name:', m3.name) #사용(속성1)
print('m3.age:', m3.age) #사용(속성2)
print('m3.addr:', m3.addr) #사용(속성3)