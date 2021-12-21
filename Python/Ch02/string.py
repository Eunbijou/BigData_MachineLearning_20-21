# 문자열
str1="문자열 공부!"
str2='string \'study!\'' #
str3='''이 문자열은
이런 의미로
사용된다.''' # 여러줄로 문자열 나타내기
print(str1)
print(str2)
print(str3)

# 문자열 곱하기 응용
str1='python study'
print("="*14)
print(" "+str1)
print("="*14)

# 문자열 슬라이싱
a="Life is too short, You need Python"
b=a[12:17] # 문자열 변수[시작위치:다음위치]
print(b)

# [ "I eat %d apples." % ]
a=10
print("I eat "+str(a)+" apples.")
print("I eat", a, "apples.")
print("I eat %d apples." % a)
print("I eat {0} apples.".format(a))

# 문자열 바꾸기
a="pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]
print(a)