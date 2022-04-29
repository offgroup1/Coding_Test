#3-2
# N,M,K 입력받기
N, M, K = map(int, input().split())
data_l = list(map(int, input().split()))
data_l.sort()

# 가장 큰 데이터가 더해지는 횟수->K*(M//K), 두번째로 큰 데이터가 더해지는 횟수->(M-K*(M//K))
result = data_l[-1]*K*(M//K)+data_l[-2]*(M-K*(M//K))
print(result)