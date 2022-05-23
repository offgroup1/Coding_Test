# 모의고사
def solution(answers):
    answer = []
    count=[0,0,0] # 세 사람이 맞춘 개수 순서대로 넣기
    person1 = [1,2,3,4,5] # 첫 번째 수포자
    person2 = [2,1,2,3,2,4,2,5] # 두 번째 수포자
    person3 = [3,3,1,1,2,2,4,4,5,5] # 세 번째 수포자

    for i in range(len(answers)): # answer와 사람들의 정답과의 비교
        if answers[i] == person1[i%5]: # 첫 번째 수포자 5개 반복
            count[0] +=1
        if answers[i] == person2[i%8]: # 두 번째 수포자 8개 반복
            count[1] +=1
        if answers[i] == person3[i%10]: # 세 번째 수포자 10개 반복
            count[2] +=1

    highest = max(count)

    for i in range(len(count)): # 같은 횟수 정답을 맞힌 경우도 처리
        if count[i]==highest:
            answer.append(i+1)
    return answer