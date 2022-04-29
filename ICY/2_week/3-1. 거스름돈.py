#3-1
N = int(input("거슬러 줘야 할 돈을 입력해주세요."))
num=0

coin_type = [500,100,50,10] # 큰 단위 거스름돈 순으로
for i in coin_type:
    num += N//i
    N=N%i

print(num)