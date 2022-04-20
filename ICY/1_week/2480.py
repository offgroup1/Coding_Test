A, B, C = map(int, input().split())

if A==B==C: # 세 숫자가 모두 같을 때
    print(10000+A*1000)
elif (A==B)|(A==C)|(B==C):  # 두 숫자가 같을 때
    if (A==B)|(A==C):  # 첫번째 숫자로 두 숫자가 같을 때
        print(1000+A*100)
    else:  # 첫번째 숫자가 아닌 수로 두 수가 같을 때 (두번째와 세번째 숫자가 같을 때)
        print(1000+B*100)
else:  # 세 숫자가 모두 다를 때
    print(max(A, B, C)*100)