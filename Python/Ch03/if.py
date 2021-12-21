#짝수 홀수 HIPO :  계층적 입력 처리 출력
#
# no=int(input("숫자 입력 : "))
#
# if(no%2==0):
#     print("%d는 짝수"%no)
#     print("이 수는 2로 나눠 나머지가 0이 되는 값")
# else:
#     print("%d는 홀수"%no)
#     print("이 수는 2로 나눠 나머지가 1이 되는 값")


#윤년
# 4위 배수 : #4의 배수
#     100의 배수 : #100의 배수
#         400의 배수 : #400의 배수
#             윤년
#          else: #100의 배수, 400의 배수가 아니다
#             평년
#          else: #4의 배수, 100의 배수가 아니다
#             윤년
#          else: #4의 배수가 아니다
#             평년

# year=int(input("연도 입력 : "))
#
# if year%4==0 and year%100!=0 or year%400==0:
#     print("{}년은 윤년!!".format(year))
# else:
#     print("{}년은 평년!!".format(year))


#과일 찾기
# fruits=['사과', '귤', '포도', '오렌지', '배']
#
# print(fruits,end='')
# instr=input("중 뭐드실? ")
#
# if instr in fruits: #not in 가능, 그러면 print 내용 반대로!
#     print("응~ 쳐먹어")
# else:
#     print("응 ~ 그거 아니야~")