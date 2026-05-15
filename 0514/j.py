#구구단
# a = 2
# for i in range(9):
#     print(str(a)+'*'+str(i+1)+'='+str(a*(i+1)))
# a = 2
# while a < 10 :
#     for i in range(9):
#         print(str(a)+'*'+str(i+1)+'='+str(a*(i+1)))
#     a += 1
# a = 2
# text = '{} * {} = {}'
# while a < 10 :
#     for i in range(9):
#         print(text.format(a,i+1,a*(i+1)), end="\t")
#     print()
#     a += 1
# text = '{} * {} = {}'
# for a in range(2,10) :
#     for i in range(9):
#         print(text.format(a,i+1,a*(i+1)), end="\t")
#     print()
# 정방향
# text = '{} * {} = {}'
# for a in range(2,10) :
#     for i in range(1,10):
#         print(text.format(a,i,a*(i)), end="\t")
#     print()
# 역방향
# text = '{} * {} = {}'
# for a in range(0,10) :
#     for i in range(2,10):
#         if a == 0 :
#             print(f'구구단 {i}단', end="\t")
#         else:
#             print(text.format(i,a,a*(i)), end="\t")
#     print()
# 2단만 출력
# text = '{} * {} = {}'
# for a in range(2,10) :
#     if a % 2 == 0:
#         for i in range(1,10):
#             print(text.format(a,i,a*(i)), end="\t")
#         print()