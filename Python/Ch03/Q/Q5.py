# student=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# sum=0
# for jum in student:
#     sum+=jum
# avg=sum/len(student)
# print("sum :",sum,"avg :",avg)\

#5-1. 임의의 개수를 입력 받아서 합계 평균 구하시오.
student=[]
while True:
    i = int(input("점수를 입력하시오. "))
    if i==0: break
    student.append(i)
print(i)

sum=0
for jum in student:
    sum += jum
avg=sum/len(student)
print("sum :",sum,"avg :",avg)