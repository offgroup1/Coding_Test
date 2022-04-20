A,B = map(int, input().split())
C = int(input()) # 더해지는 분
D = B+C # 더해진 시간

if D>=60: # 더해진 시간을 단위에 맞게 정리
    A = A+(D//60)
    D = D%60
if A>=24: # 24시 이상이 되면 다시 0부터 시작
    A=A-24
print(A, D)