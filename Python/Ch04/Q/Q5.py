# 사용자의 입력을 파일에 저장하는 프로그램을 작성해보다
# 단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다
f1 = open("test.txt", 'w')
f1.write("Life is too short")
# f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
# f2.close()

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())