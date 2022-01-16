# slot machine 문제 (20220116)

import random

slot1 = random.randint(33, 39)

# step1) 슬롯머신 홈화면
while True:
    select = int(input('입장하시겠습니까? 입장하기: 1 // 그만하기: 2 >> '))
    if select == 1 :
        while True:
            print('<SLOT MACHINE>')
            num = int(input('코인넣기: 1 // 그만하기: 2 >> '))
            if num == 1:
                slot = [random.randint(33, 39), random.randint(33, 39), random.randint(33, 39)]
                print('%c | %c | %c ' % (slot[0], slot[1], slot[2]))

                if slot[0] == slot[1] == slot[2]:
                    print('터졌다 터졌다 잭팟~!!🎉🎊🎉')
                    print()
                else:
                    print('실패...')
                    print()

            elif num == 2:
                print('게임을 종료합니다.')
                break

            else:
                print('잘못 입력하셨습니다.')
                print()

    elif select == 2:
        print('안녕히가세요.')
        break

    else:
        print('잘못 입력하셨습니다.')
        print()











