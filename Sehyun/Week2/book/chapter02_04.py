# -*- coding: utf-8 -*-
"""chapter02_04

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zzspn0K2Kcm5zqcxjlfBTO2VujXWOTsr
"""

N, K = map(int,input().split())

result = 0

while N !=1:
    if N % K != 0:
        N = N-1
        result +=1
    else:
        N = N/K
        result +=1

print(result)

