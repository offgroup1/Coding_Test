# -*- coding: utf-8 -*-
"""1330

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ArhJyKO2fFlMBk1qWFDQyP33tz5XYDq2
"""

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')

