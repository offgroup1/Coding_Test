# -*- coding: utf-8 -*-
"""chapter02_02

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J8fcfhLmr6cOKt75EHmeCyHmEEcIebqH
"""

#큰 수의 법칙
N,M,K = map(int, input().split()) #배열 숫자 갯수, 총 더하는 횟수, K는 인덱스가 같은 것을 연속성 사용 시 최대 횟수

array1 = list(map(int, input().split()))

array1.sort()

#인덱싱으로 설정하는 이유는, 같은 수여도 인덱싱이 다르면 다른 숫자 취급
#최대, 두번째 큰 수라고 보긴 어려울 수도 있다
#max함수를 사용하면 안되는 이유

first = array1[N-1] 
second = array1[N-2]

sum1 = 0 # first,second의 총 합

while True: # 무한 루프 차피 아래에서 조건 맞으면 내보내면 되니끼

    for i in range(K):#K번 만큼 더함
        if M == 0: #M이 0 이라는 것은 입력으로 주어지는 K보다 항상 크다의 반례로 While문 탈출
            break #탈출
        
        sum1 +=first
        M -= 1 # 더해지는 횟수 차감
        
    if M == 0:
        break
        
    sum1 += second
    M -=1

print(sum1)

for i in range(3):
    print(1)

#큰 수의 법칙 version2
#이중 for문이라 시간은 오래 걸릴 수도 있다.
N,M,K = map(int, input().split()) #배열 숫자 갯수, 총 더하는 횟수, K는 인덱스가 같은 것을 연속성 사용 시 최대 횟수

data = list(map(int, input().split()))

data.sort(reverse=True)

#인덱싱으로 설정하는 이유는, 같은 수여도 인덱싱이 다르면 다른 숫자 취급
#최대, 두번째 큰 수라고 보긴 어려울 수도 있다
#max함수를 사용하면 안되는 이유

f1 = data[0] 
f2 = data[1]

result = [] # 빈 리스트 후 

for j in range(int(M % K)):
    for i in range(K):
        result.append(f1)
    result.append(f2)

print(sum(result))

8 % 3

