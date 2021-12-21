# 구구단 출력

i=1

dan=2
while dan<10:
    print(" %ddan  "%dan, end="")
    dan+=1
print()
print("="*56)

while i<10:
    j=2
    while j<10:
        # print("%d*%d=%d "%(j,i,j*i),end="")
        print("{}*{}={:2} ".format(j, i, j * i), end="")
        j+=1
    i+=1
    print()
