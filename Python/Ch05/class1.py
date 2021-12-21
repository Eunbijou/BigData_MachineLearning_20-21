# 객체의 기본적인 출력 문장은 __str__로 만들고,
# 객체명만 입력하면 __str__이 실행된다, 오버라이딩이라 함
# 파이썬에는 오버로딩 X, 기능은 동일하나 형식이 다른 경우는 있음

class Car:
    def __init__(self, color = '', door = 4):
        self.color = color
        self.door = door
        self.speed = 0

    def accelator(self):
        self.speed += 10

    def breaker(self):
        if self.speed == 0:
            print("차가 멈췄다.")
        else:
            self.speed -= 10

    def __str__(self):   # 객체 명만 호출했을 떄 출력될 문자열을 반환해주는 시스템 메서드
        name = "이 붕붕이는 color는 "+self.color+", door의 개수는 "+str(self.door)+"인 차입니다."
        return name


js = Car()
# JS.color = "Red"
# JS.door = 5
js = Car("Red", 5)
print("꼬마버스타요의 색은 %s, 문은 %d개"%(js.color, js.door))
js.accelator()
print("꼬마버스타요의 속도는 {}KM".format((js.speed)))
while True:
    js.accelator()
    print("꼬마버스타요의 속도는 %dKM"%(js.speed))
    if js.speed >= 80: break
print(js)

ys = Car("Red", 2)
ys.color = "Black"
print("빵빵덕의 붕붕이 색은 %s, 문은 %d개"%(ys.color, ys.door))
ys.accelator()
print("빵빵덕의 속도는 {}KM".format((ys.speed)))
while True:
    ys.accelator()
    print("빵빵덕의 속도는 %dKM"%(ys.speed))
    if ys.speed >= 80: break
print(ys)

class Truck(Car):
    def __init__(self, w = 1000):
        Car.__init__(self, "darkblue", 2)
        self.maxWeight = w
        self.weight = 0

    def load(self, w):
        if self.weight + w <= self.maxWeight:
            self.weight += w
        else:
            print((self.weight+w) - self.maxWeight, "중량초과")
        return self.weight

    def unload(self, w):
        self.weight -= w
        return self.weight

    def __str__(self):
        return self.color + " " + str(self.door) + " "+ str(self.weight) + " / "+str(self.maxWeight)

forter = Truck()
titan = Truck(5000)

forter.load(500)
forter.load(800)
print(forter)
# print(forter.door, forter.speed)

titan.load(4000)
titan.load(2000)
titan.unload(1000)
titan.load(2000)
print(titan)



