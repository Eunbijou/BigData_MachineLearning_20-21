# name=input("이름 : ")
# jum=list(map(int,input("국어 영어 수학 : ").split(',')))
# print(name, jum)

inData=input("이름 국어 영어 수학")
print(inData)
sData=inData.split()
print(sData)
name=sData[0]
jumsu=map(int,sData[1:4])
print(name, jumsu)
