# 리스트 내포

a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result=[num*2 for num in a]
print(result)
result=[num*2 for num in result if num % 2 == 0]
print(result)