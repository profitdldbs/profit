# Ai반 2기 python 중급반 - 11주차 정규수업(16:30~18:30) mission
'''
[수업을 시작하기 전에!]
1. 웨일ON으로 원격 회의실 접속하기
2. NAS 서버 접속(접속이 안될 경우 말해주기~)
3. 탐색기를 활용하여 내가 현재 작업하고 있는 파일 경로 열어두기
4. Pycharm 수업 코드 다운로드 받아 열어두기~
5. 수업시간 집중~~~!! 딴 짓! 멈춰~~~~~!
'''

# Problem 1: 더하기 사이클

import copy

N = int(input())
dummy = copy.copy(N)
yoon = 0

# 두자리수 만들기
if dummy < 10:
    dummy *= 10


while True:
    ten = dummy % 10
    one = ((dummy // 10) + (dummy % 10)) % 10
    dummy = ten*10 + one
    yoon += 1
    print('dummy', dummy)

    if N == dummy:
        break
print(yoon)


# Problem 2: 평균은 넘겠지


# Problem 3: 셀프 넘버


# 추가 문제: ACM 호텔

