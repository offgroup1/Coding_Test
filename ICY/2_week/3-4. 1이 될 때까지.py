# 3-4
# N,K의 형태 입력받기
N, K = map(int, input().split())

count = 0
while N!=1: # N이 1이 될 때까지 실행
    if N%K == 0: # N이 K로 나누어 떨어질 때
        N = N//K
    else: # N이 K로 나누어 떨어지지 않을 때
        N=N-1
    count += 1
    
print(count)