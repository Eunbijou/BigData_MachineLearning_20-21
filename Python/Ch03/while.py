# 1~100까지 출력, 한 줄에 10개씩 출력(while문)
# i=1
# while i<=100:
#         print("%4d"%(i), end="")
#         if (i % 10 == 0):
#             print()
#         i+=1
# print("  다했다.")


# 1부터 무한 증가
i=1
while 1:
    print("%d",i)
    if(i>=1000) :break
    i+=1
print()
i=1
while i<=1000:
    print("%d"%(i), end="")
    i +=1