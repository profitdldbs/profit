## 가위바위보
'''
import random
RSP = ['가위', '바위', '보']
computer = random.choice(RSP)

comwin = 0
plwin = 0

while comwin < 2 and plwin < 2:
    player = input('가위 바위 보!! ')
    computer = random.choice(RSP)
    if RSP:
        if (player == '가위' and computer == '보' ) or (player == '바위' and computer == '가위' ) or (player == '보' and computer == '바위' ):
            print('니가 이김')
            plwin += 1

        elif (player == '가위' and computer == '바위' ) or (player == '바위' and computer == '보' ) or (player == '보' and computer == '가위' ):
            print('컴퓨터도 못 이기냐')
            comwin += 1

        else:
            print('비김')
    else:
        print('다시해')

while comwin >= 2 and plwin >= 2:
    break
'''

## 달팽이는 올라가고 싶어
'''
A, B, V = map(int, input().split())
now = 0
days = 0

while True:
    days += 1
    now += A
    if now >= V:
        print(days)
        break

    else:
        now -= B
'''
## 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)
c = 0

for i in range(N):
    c += A[i] * B[i]
    print()






