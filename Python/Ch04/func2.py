# #매개변수 개수가 일정x
def average(*score):
    sum = 0
    for jum in score:
        sum += int(jum)
    avg = sum / len(score)
    return sum, avg
sum, avg = average(1,2,3,4,5,6)
print("sum :",sum," avg :",avg)