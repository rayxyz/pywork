msg = 'fsd' 'sdfd'
print msg

words = ['hello', 'world', 'mother', 'fucker']
print 'lenth of words => ' + str(len(words))
for word in words:
    print word

for i in range(len(words)):
    print i, words[i]

class GoodClass:
    pass

def say_hello(name, msg='Hello world!'):
    print name + ' says: ' + msg

say_hello('xiaoming')

def add_nums(m):
    return lambda y: y * m

f = add_nums(10)
print f(2)
print f(10)

tup = 1, 3, 4, 35, 5
tup0 = tup, (435, 6, 5)
print tup0

si = 'gooo',
print len(si), si

data = ['fsdf', 'dsf', 'dsf', 'ddd','fff']
data = set(data)
print data

for i, v in enumerate(data):
    print i, v

for v in sorted(set(data)):
    print v

try:
    i = 2 / 0
except:
    print 'Exception...'


class Animal:
    def _init_(self):
        print 'Initializing...'

    def walk(self, distance=100):
        print 'The animal is walking with distance => ' + str(distance) + ' meters.'

    def eat(self):
        print 'It is eating time.'

class Monkey(Animal):
    def walk(self, distance=1000):
        print 'The funny monkey is wanting to walk ' + str(distance) + ' meters.'

anim = Animal()
anim.walk()
monkey = Monkey()
monkey.walk()
monkey.eat()

def generator_generate():
    array = {1, 4324, 545, 4, 34, 545, 3, 0, -56, 43, 32, -23}
    y = sum(x*x for x in array)
    print y

generator_generate()
