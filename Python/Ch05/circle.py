# 클래스를 이용하여 반지름을 이용하여 원넓이, 둘레를 출력하시오
class Circle:
    pi=3.14
    def __init__(self):
        self.radius=0
        self.area=0
        self.periphery=0

    def setData(self,r):
        self.radius=r

    def areac(self):
        self.area=self.radius * self.radius * self.pi
        return self.area

    def peripheryc(self):
        self.periphery=2*self.radius*self.pi
        return self.periphery

c1 = Circle()
c2 = Circle()
c3 = Circle()

c1.setData(3)
c2.setData(5)
c3.setData(7)

print(c1.radius, c1.areac(), c1.peripheryc())
print(c2.radius, c2.areac(), c2.peripheryc())
print(c3.radius, c3.areac(), c3.peripheryc())
