# 입국심사
# 방법1
"""
def solution(n, times):
    answer = 0
    multiple_num_list = []

    for i in times:
        for j in range(1,n+1):
            multiple_num_list.append(i * j)
            # multiple_num_list에 한 명 한 명 끝나는 시간을 넣기
    multiple_num_list.sort() # 순서대로 정렬하기

    answer = multiple_num_list[n-1]
    return answer # 모든 사람이 심사를 받는 데 걸리는 시간의 최솟값

"""

# 방법2
def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n  # 가장 효율적으로 검사했을 때, 가장 비효율적으로 검사했을 때

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time  # 모든 심사관들이 mid분 동안 심사한 사람의 수
            if people >= n:  # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나감
                break
        if people >= n:  # 심사한 사람의 수가 심사 받아야 할 사람의 수보다 많거나 같은 경우
            answer = mid
            right = mid - 1
        elif people < n:  # 심사한 사람의 수가 심사 받아야할 사람의 수보다 적은 경우
            left = mid + 1

    return answer