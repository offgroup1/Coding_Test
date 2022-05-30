# -*- coding: utf-8 -*-
"""20220531

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v5eGPh75Pf9heZaK7gObGMnp6jBG7Fgl

부품찾기
"""

import sys
import bisect # store에서 손님이 요구한 물품 x를 삽입할 위치 인덱스 반환
si = sys.stdin.readline
 
n = int(si())
store = sorted(map(int, si().split()))
m = int(si())
wish = list(map(int, si().split()))
 
    for x in wish:
        idx = bisect.bisect_left(store, x)
 
        if store[idx] == x:
            print('yes', end = ' ')
        else:
            print('no', end = ' ')

"""떡볶이 떡 만들기

"""

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def binary_search(array, target, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        # 현재 절단기 위치에 따른 떡 길이의 총합
        for i in array:
            if i > mid:
                total += i - mid

        # 떡 길이가 부족하면 절단기를 왼쪽으로 이동
        if total < target:
            end = mid - 1
        # 떡 길이가 충분하다면 절단기를 오른쪽으로 이동
        else:
            start = mid + 1
            result = mid

    return result


print(binary_search(height, m, 0, max(height)))
출처: https://ddu0422.tistory.com/90 [History:티스토리]