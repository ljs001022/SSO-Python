# 역방향
# text = '{} * {} = {}'
# for a in range(0,10) :
#     for i in range(2,10):
#         if a == 0 :
#             print(f'구구단 {i}단', end="\t")
#         else:
#             print(text.format(i,a,a*i), end="\t")
#     print()
# 보기 좋게 출력 위에서 아래로 향하게
text = '{} * {} = {}'
for a in range(0,10) :
    for i in range(2,10):
        if a == 0 :
            print(f'구구단 {i}단', end="\t")
        else:
            print(text.format(i,a,a*(i)), end="\t")
    print()
# 2단만 출력
# text = '{} * {} = {}'
# for a in range(2,10) :
#     if a % 2 == 0:
#         for i in range(1,10):
#             print(text.format(a,i,a*(i)), end="\t")
#         print()
# 2단만 출력
# text = '{} * {} = {}'
# for a in range(2,10) :
#     if a % 2 == 0:
#         for i in range(1,10):
#             print(text.format(a,i,a*i), end="\t")
#         print()
# 홀수 스텝만 출력
# text = '{} * {} = {}'
# for a in range(2,10) :
#     for i in range(1,10):
#         if i % 2 == 1:
#             print(text.format(a,i,a*i), end="\t")
#     print()
# 리버스 출력
# text = '{} * {} = {}'
# for a in range(9, 1, -1) :
#     for i in range(9, 0, -1):
#         print(text.format(a,i,a*i), end="\t")
#     print()
# continue, break 활용 // 짝수단만 + 짝수곱스킵 + 결과값이 40이 넘으면 강제종료
# text = '{} * {} = {}'
# for a in range(2,10) :
#     if a % 2 == 1:
#         continue
#     for i in range(1,10):
#         if i % 2 == 0:
#             continue
#         print(text.format(a,i,a*i), end="\t")
#         if a * i > 55:
#             print('위험수위 도달!!')
#             break
#     else:
#         print()
#         continue
#     break
# while 문 사용할것
# text = '{} * {} = {}'
# a = 2
# while a < 10:
#     if a % 2 == 1:
#         a += 1
#         continue
#     i = 1
#     while i < 10:
#         if i % 2 == 0:
#             i += 1
#             continue
#         result = a * i
#         print(text.format(a, i, result), end="\t")
#         if result > 40:
#             print('위험수위 도달!!')
#             break
#         i += 1
#     else:
#         print()
#         a += 1
#         continue
#     break