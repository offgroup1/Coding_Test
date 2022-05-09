def solution(array, commands):
    answer = []
    for i in commands:
        selected_array = array[i[0]-1:i[1]] # i~j까지의 범위의 새 배열 만들기
        selected_array.sort() # 배열 정렬하기
        answer.append(selected_array[i[2]-1]) # 배열의 k번째를 뽑아내기
    return answer