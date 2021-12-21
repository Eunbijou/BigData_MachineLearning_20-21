# # 1~100 사이의 소수와 개수 출력
# i=2
# primeNoCnt=0
# loofCnt=0
# while i<=100:
#     j=2
#     sw=0 #나누어 떨어진 여부 판단
#     while j<i:
#         loofCnt+=1
#         if i%j==0:
#             sw=1
#             break
#         j+=1
#     if sw==0:
#         print("prime No=", i)
#         primeNoCnt += 1
#     i+=1
#
# print("prime no counter : %d"%(primeNoCnt))
# print("loof counter : %d"%(loofCnt))

import math

i=2
primeNoCnt=0
loofCnt=0
while i<=100:
    j=2
    sw=0 #나누어 떨어진 여부 판단
    while j<=i/2:
        loofCnt+=1
        if i%j==0:
            sw=1
            break
        j+=1
    if sw==0:
        print("prime No=", i)
        primeNoCnt += 1
    i+=1

print("prime no counter : %d"%(primeNoCnt))
print("loof counter : %d"%(loofCnt))
