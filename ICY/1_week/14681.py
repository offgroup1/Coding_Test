A,B = map(int, input().split())

if (A>0)&(B>0):
    print(1)
elif (A<0)&(B>0):
    print(2)
elif (A<0)&(B<0):
    print(3)
else:
    print(4)

"""
좌표 (A,B)에서
A 양수, B 양수 -> 1사분면
A 음수, B 양수 -> 2사분면
A 음수, B 음수 -> 3사분면
A 양수, B 음수 -> 4사분면
"""