name = '종섭'
age = 27

str = '나는 이름이 '+name+'이고, 나이가 '+str(age)+'살이다'
print(str)

strformat = '나는 이름이 {}이고, 나이가 {}살이다'
print(strformat.format(name, age))

strformat2 = '나는 이름이 {1}이고, 나이가 {2}살이고 {0}에 산다'
print(strformat2.format('광명', name, age))

strfloat = '나는 급여를 ${:.2F}를 받고 싶어'
print(strfloat.format(456.12512))

strformat3 = '나는 {com}의 {car}를 갖고 싶어'
print(strformat3.format(com='람보르기니', car='부가티'))