a = int(input())

if (a %4==0)&(a%100!=0)|(a%400==0):
    print(1)
else:
    print(0)
# 윤년이면 1, 아니면 0 출력