def fab(maxium):
    n, a, b = 0, 0, 1
    while n < maxium:
        #print b
        yield b
        a, b = b, a + b
        n += 1


fab(6)
for n in fab(7):
    print n,


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


o = odd()
print o.next()

# This is the end
