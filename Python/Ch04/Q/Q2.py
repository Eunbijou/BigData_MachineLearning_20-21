 def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
     result = 0
     for i in args:
        result += i
     return result / len(args)
