# -*- coding: utf-8 -*-
"""10430

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fkrsWCvHXWPxYCWiEAat7b-SyjZHYDW0
"""

A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

