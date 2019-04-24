#########################################
#  OBJECTS
#########################################


import itertools


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
#  Inheritance
##################################

class G(object):
    gG = 1234


class H(G):
    hH = 4321


g = G()
h = H()

print(g.gG, " ", h.gG, " ", h.hH)


class I(object):
    def __init__(self):
        a = 4
        b = 5


class J(I):
    def __init__(self):
        aa = 44


i = I()
j = J()
print(i.__dict__)


##############################
# Exceptions
##############################

alist = []


def alistAdd(add):
    try:
        alist.append(int(add))
    except ValueError:
        print('err')


alistAdd('stringhere')


try:
    1/0
except (ValueError, TypeError):
    print('value error')
except ZeroDivisionError:
    print('zero devision')
except ArithmeticError:
    print('arithmetic error')
except Exception:
    print('exception')
else:
    print('all good')
finally:
    print('complete')


class myException(Exception):
    print('My Exception')


try:
    raise myException()
except myException:
    print("hi")

########################
#  iterators
########################

alist = [1, 2, 3, 4]
aiter = iter(alist)
print(aiter)


a = [x for x in range(10)]
print(a)
b = itertools.accumulate(a)
b = list(b)
print(b)

print(list(itertools.combinations('abcd', 3)))
print(list(itertools.combinations_with_replacement('abcd', 3)))
print(list(itertools.permutations(['a', 'b', 'c'])))
print(list(itertools.dropwhile(lambda x: x < 4, a)))
print(list(itertools.filterfalse(lambda x: x < 4, a)))
print(list(itertools.product('abc', 'xy')))

#########################
# generators
#########################


def doGenerate1():
    while True:
        yield 1


print(doGenerate1())
print(next(doGenerate1()))

def doGenerate2():
    alist = range(3)
    for i in alist:
        yield i*i


gen2 = doGenerate2()
gen22 = doGenerate2()
gen222 = doGenerate2()
for i in gen2:
    print(i)

print(next(gen22))
print(next(gen22))
print(next(gen22))
print(list(gen222))
print(list(gen222))


##########################
# decorate
##########################