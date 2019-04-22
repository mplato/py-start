#########################################
#  OBJECTS
#########################################
class A(object):
    pass


class B(object):
    x = 1


a = A()
b = B()

print(b.x)


class C(object):
    total = 10
    _hidden = 73

    def getRemaining(self):
        return self.total


c = C()
print(c.total)
print(c.getRemaining())

c.total -= 1
print(c.total)
print(c.getRemaining())

del c.total
print(c.total)
print(c.getRemaining())


class D(object):
    def __init__(self, x=3, y=2):
        self.plus = x + y
        self.minus = x - y


d = D(10, 1)
print(d.plus, " ", d.minus)


class E(object):
    __slots__ = ('plus')

    def __init__(self, x=3, y=2):
        self.plus = x + y
        #self.minus = x - y


e = E(7, 3)


class F(object):
    def __init__(self, x, y):
        self.x = x + y

    def __call__(self, x, y):
        return x + y


f = F(77, 11)
print(f.x)

print(f(777, 111))


##################################
#  RECURSION
##################################