## 연습문제-구구단 출력하기
'''
for i in range(1,10):
    for j in range(2,10):
        print(f'{i} * {j} =',i*j)
'''

## 소수 구하기
'''
x = int(input())
number = list(map(int, input().split()))
sosu = 0

for N in number:
    is_prime = True
    if N > 1 :
        for i in range(2,N):
            if N % i == 0:
                is_prime = False
        if is_prime == True:
            sosu += 1

print(sosu)
'''

## 팩토리얼
'''
num = int(input())
fac = 1
for i in range(1,num+1):
    fac *= i
print(fac)
'''

## 부녀회장이 될테야
'''
test = int(input())

for i in range(test):
    floor = int(input())
    ho = int(input())
    f_n = list(range(1,ho+1))

    for i in range(floor):
        for j in range(ho):
            f_n[j] += f_n[j-1]
        print(f_n)
    print(f_n[-1])
'''

## 자동판매기
'''
money = int(input('지불한 돈을 입력>> '))
drink = int(input('구입할 음료수 가격 입력>> '))

change_money = money - drink
print(f'거스름돈은 {change_money}원 입니다.')

change_1000 = change_money // 1000
change_500 = (change_money % 1000) // 500
change_100 = (change_money % 500) // 100

print(f'1000원 지폐의 수 => {change_1000}')
print(f'500원 지폐의 수 => {change_500}')
print(f'100원 지폐의 수 => {change_100}')
'''