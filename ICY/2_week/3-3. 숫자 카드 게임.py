#3-3
# N,M의 형태 입력받기
N, M = map(int, input().split())

result=0
# 숫자 전체 한줄씩 입력받기
for i in range(N):
    data = list(map(int, input().split()))
    min_num = min(data) # 한 줄의 최소값 저장하기
    result = max(result, min_num) # 최소값들 중 가장 큰 값 찾기
    
print(result)