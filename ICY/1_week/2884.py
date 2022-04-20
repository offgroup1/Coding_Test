H, M = map(int, input().split())

if H==0:
    H=24  # 0시일 때를 24시라고 생각하고 계산

if M>=45:  # M이 45보다 클 때는 H가 바뀌지 않음
    if H==24:  # 24시일 때는 0으로 나타냄
        print(0, M-45)
    else:
        print(H, M-45)
else:  # M이 45보다 작을 때는 M이 1작아짐
    print(H-1,M+15)
