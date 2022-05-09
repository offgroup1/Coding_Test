N = int(input("학생의 수를 입력하세요."))
student_l = []

for i in range(N): # 데이터 입력받은 것을 이름, 성적으로 나누기
    data = input().split()
    student_l.append((data[0], int(data[1])))

student_l = sorted(student_l, key = lambda student : student[1])
# student의 성적을 key로 준 후 오름차순으로 정렬하기

for i in student_l:
    print(i[0], end=' ') # 이전 출력값에 이어서 출력하기