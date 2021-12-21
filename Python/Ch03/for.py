# 1~100까지 출력, 한 줄에 10개씩 출력(for문)
#
# for i in range(1,101,1):
#     print("{:4}".format(i), end="")
#     if(i%10==0):
#         print()
# print("다했다.")


#구구단(for문)
for dan in range(2,10):
    print(" %ddan  "%dan, end="")
print()
print("="*56)

for i in range(1,10):
    for j in range(2,10):
        print("{}*{}={:2}".format(j,i,j*i), end="")
    print()