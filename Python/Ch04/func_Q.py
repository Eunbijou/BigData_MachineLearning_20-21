# 숫자 한 개를 매개변수로 받아 짝수/홀수 여부 출력
## def mod(no):
##
##     if no%2==0:
##         print("%d는 짝수"%no)
##         print("이 수는 2로 나눠 나머지가 0이 되는 값")
##     else:
##         print("%d는 홀수"%no)
##         print("이 수는 2로 나눠 나머지가 1이 되는 값")
## mod(5)

# def isEvenOdd(parml):
#     if parml%2==1:
#         print("%d is odd!"%parml)
#     else:
#         print("%d is even!"%parml)
#
# inData=int(input("enter a no : "))
# isEvenOdd(inData)

# 1번 문제를 이용해 함수에서 입력 받아서 출력
# def mod(no):
#         no = int(input("숫자 입력 : "))
#
#         if no % 2 == 0:
#             print("%d는 짝수" % no)
#             print("이 수는 2로 나눠 나머지가 0이 되는 값")
#         else:
#             print("%d는 홀수" % no)
#             print("이 수는 2로 나눠 나머지가 1이 되는 값")
# mod(0)


# 1번 문제를 이용해 리턴한 값으로 출력
# def is_odd(no):
#      if no % 2 == 1:   # 2로 나누었을 때 나머지가 1이면 홀수이다.
#          return True
#      else:
#          return False
# print(is_odd(2))

# def isEvenOdd(parml):
#     if parml % 2 == 1:
#         print("%d is odd!" % parml)
#     else:
#         print("%d is even!" % parml)
#
#
# inData = int(input("enter a no : "))
# isEvenOdd(inData)

# 소수 구하기를 함수를 이용해 구하시오.
# import math
#
# def primeNo(start=2, maxValue=100, loofCnt=0, primeNoCnt=0):
#     i=start
#     while i<=maxValue:
#         j=2
#         sw=0 #나누어 떨어진 여부 판단
#         while j<math.sqrt(i):
#             loofCnt+=1
#             if i%j==0:
#                 sw=1
#                 break
#             j+=1
#         if sw==0:
#             print("prime No=", i)
#             primeNoCnt += 1
#         i+=1
#     return loofCnt,primeNoCnt
#
# i=2
# primeNoCnt, loofCnt=primeNo()
# print("1 to 100 prime no counter : %d"%(primeNoCnt))
# print("1 to 100 loof counter : %d"%(loofCnt))
#
# primeNoCnt, loofCnt=primeNo(maxValue=10)
# print("1 to 100 prime no counter : %d"%(primeNoCnt))
# print("1 to 100 loof counter : %d"%(loofCnt))

# 구구단의 단은 매개변수로 받아 재작성하시오.
def gugudan(dan):
    i=1
    print("{}단".format(dan))
    while(i<10):
        print("%d*%d=%2d"%(dan,i,dan*i))
        i+=1

inData=int(input("단 입력 : "))
gugudan(inData)