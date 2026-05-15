import numpy as np

roop = True
rcplist = ['가위', '바위', '보']
result = ['무승부','a승', 'b승']

print("a와 b가 비길때까지 가위바위보를 시작합니다")
while roop:
    a = np.random.randint(low=0, high=3)
    b = np.random.randint(low=0, high=3)
    winner = 0
    print('a는 '+rcplist[a]+'를 냈고, b는 '+rcplist[b]+'를 냈습니다.')
    if a == 0:
        if b==0:
            roop = False
        elif b==1:
            winner = 2
        elif b==2:
            winner = 1
    elif a == 1:
        if b==0:
            winner = 1
        elif b==1:
            roop = False
        elif b==2:
            winner = 2
    elif a == 2:
        if b==0:
            winner = 2
        elif b==1:
            winner = 1
        elif b==2:
            roop = False
    print('결과는!!!! '+result[winner])
