# a=1
# def vartest(ina):
#     ina = ina +1
#     print("in :",ina)
#
# vartest(a)
# print("out :",a)

# def vartest(a):
#     a = a + 1
#     return a
#
# a=vartest(3)
# print(a)

#전역변수, 단 꼭 필요한 곳이 아니면 사용X
a=1
def vartest():
    global a #바깥에 있는 변수 a를 여기서 사용
    a = a+1
vartest()
print(a)