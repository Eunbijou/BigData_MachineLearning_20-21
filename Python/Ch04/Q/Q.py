# test1.txt 파일과 test2.txt 파일을 합쳐서 test0.txt 파일을 만드시오.
# 앞의 두 개의 파일에 임의의 내용을 포함하게 하시오.

f1=open("test1.txt","w")
f1.write("준서야 공부하자\n")
f1.write("준서야 그만 자라\n")
f1.close()

f2=open("test2.txt","w")
f2.write("영서는 열공하네?\n")
f2.write("나도 열공할게\n")
f2.close()

f1 = open("test1.txt", 'r')
f2 = open("test2.txt", 'r')
f3=open("test0.txt", 'w')

str1=(f1.read())
str2=(f2.read())

f3=open("test0.txt","w")
f3.write(str1+str2)

f1.close()
f2.close()
f3.close()

f3=open("test0.txt", "r")
print(f3.read())
f3.close
