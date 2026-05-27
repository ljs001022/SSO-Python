#(미션) 1~100까지의 총합, 짝수합, 홀수합을 출력해보세요
# a = 1
# sum = 0
# esum = 0
# osum = 0
# while a<=100:
#     sum += a
#     if a % 2 == 0:
#         esum += a
#     else:
#         osum += a
#     a += 1
# print('1~100 총합은 '+str(sum)+'이고 짝수합은 '+str(esum)+' 홀수합은 '+str(osum)+'입니다.')
a = 1
sum = [0, 0, 0]
while a<=100:
    sum[0] += a
    if a % 2 == 0:
        sum[1] += a
    else:
        sum[2] += a
    a += 1
print('1~100 총합은 '+str(sum[0])+'이고 짝수합은 '+str(sum[1])+' 홀수합은 '+str(sum[2])+'입니다.')