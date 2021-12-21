# f = open('test.txt', 'r')
# body = f.read()
# f.close()
#
# body = body.replace('java', 'python')
#
# f = open('test.txt', 'w')
# f.write(body)
# f.close()

f1 = open("test.txt", 'r')
content=f1.open
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'w')
print(f2.read())
f2.close()