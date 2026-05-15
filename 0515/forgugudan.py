# 정방향
# text = '{} * {} = {}'
# for a in range(2,10) :
#     for i in range(1,10):
#         print(text.format(a,i,a*(i)), end="\t")
#     print()
#역방향
text = '{} * {} = {}'
for a in range(0,10) :
    for i in range(2,10):
        if a == 0 :
            print(f'구구단 {i}단', end="\t")
        else:
            print(text.format(i,a,a*(i)), end="\t")
    print()