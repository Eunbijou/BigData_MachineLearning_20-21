# # 리스트 생김새
# e = [1, 2, ['Life', 'is']]
# print(e[0])
# print(e[1])
# print(e[2])
# print(e[2][0])
#
# # 리스트 일부 변경
# e[2][0]='are'
# print(e[2][0])
# print(e[2][1])
#
# #리스트 요소 수정과 삭제, 추가
# a=[1,2,'b']
# a.append('a') # => [1,2,'b','a']
# print(a)
# a.insert(3,10) # => [1,2,'b',10,'a']
# print(a)
# del a[2] # => [1,2,10,'a']
# print(a)
# a.remove(2) # => [1, 2, 10, 'a']
# print(a)
#
# out=0
# #out=a.pop()
# #print("a.pop() data",out)
# print("a.pop() data =>%c"%(a.pop())) # => [1, 10, 'a']\
#
# #딕셔너리
# dic={0:10, 1:20, 2:30, 3:40, 4:50}
# del dic[3]
# print(dic)
#
# list={10,20,30,40,50}
# del dic[3]
# print(list)
# print(list[0])

# d1={1:'apple', 2:'orange'}
# d2={1:'apple', 1:'orange'}
# d3={1:'apple', 2:'apple'}
# print(d1)
# print(d2)
# print(d3)
# print("d3.get(2):",d3.get(2))
#
# d3var=d3.get(2)
# print("d3.get(2):","fruit=>"+d3var)

#집합 자료형
s1=set([1,2,3])
s2=set([3,2,1])
print((s1==s2))

#변수
# a=int(input("숫자를 입력하시오 ->"))
# b=a*100
# print(a,b)

#from copy와 copy.copy 구분
# import copy
# a=[1,2,3]
# # b=a
# # b[0]=10
# b=copy.copy(a)
# print("a의 주소{}, b의 주소{}, 값=a{}. b{}".format(id(a), id(b),a,b))

# a,b=(1,2)
# print("a={}, b={}")
