N, K = map(int, input().split()) # 원소의 개수 N, 바꿔치기 연산 K번
A = list(map(int, input().split())) # 배열 A, 배열 B를 입력받기
B = list(map(int, input().split()))

A.sort() # A는 오름차순 정렬, B는 내림차순 정렬
B.sort(reverse=True)

for i in range(K): # A의 i번째 수가 B보다 작으면 교체하기
    if A[i]<B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))