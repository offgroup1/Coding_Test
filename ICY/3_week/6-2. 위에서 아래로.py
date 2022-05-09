N = int(input("수열의 크기를 입력하세요.")) # 수열의 크기 입력하기
array = []
for i in range(N): # 숫자 입력받기
    array.append(int(input()))

array = sorted(array, reverse=True) # 내림차순 정렬
for i in array:
    print(i)