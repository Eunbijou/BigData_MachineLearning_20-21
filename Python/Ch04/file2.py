f=open("test.txt","r")

for i in range(0,5):
    inData=f.readline()
    print(inData, end='')
