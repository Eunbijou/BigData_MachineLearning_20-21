cnt = 0
while True:
    cnt += 1
    print(str(cnt)+"번째 수행")
    a = [1, 2]
    try:
        print(a[3]) # 인덱스 범위 초과
    except Exception as e:
        print(e)
    try:
        print(4/0) # 0으로 나누기 오류
    except Exception as e:
        print(e)
    finally:
        print("오류처리였습니다")
         
    if cnt == 5: break;
