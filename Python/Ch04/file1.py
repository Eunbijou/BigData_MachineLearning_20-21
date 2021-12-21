f=open("test.txt","w")
f.write("TEST FILE OPEN WRITE TEST!!!\n")
f.write("ARE YOU OK?\n")
for i in range(0,3):
    inData=input("이름 국어 영어 수학")
    f.write(inData+"\n")
f.close()