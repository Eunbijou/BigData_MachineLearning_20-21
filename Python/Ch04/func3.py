# def f1(**table):
#     print(table)
#
# print("**두 개가 있는 함수 호출")
# f1(a=1, b=2, c=3) #딕셔너리 형태의 매개변수
# f1(name='hong')

def f1(plqy=True, **table):
    if not(plqy):return
    print(table)

print("**두 개가 있는 함수 호출")
f1(False, a=1, b=2, c=3) #딕셔너리 형태의 매개변수
f1(name='hong')
