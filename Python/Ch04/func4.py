def say_myself(name, man=True, old=7):
    print("나의 이름은 %s 입니다."%name)
    print("나이는 %d살 입니다."%old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("둘리", 7)
say_myself("공실이", False, 5)