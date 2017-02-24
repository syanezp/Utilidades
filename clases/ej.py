# -*- coding: utf8 -*-
class A(object):

    def __init__(self):
        print "A"
        super(A, self).__init__()

class B(A):
    def __init__(self):
        print "B"
        super(B, self).__init__()

for x in B.__mro__:
	print x.__name__

print "__mro__:", [x.__name__ for x in B.__mro__]
instance = A()
ins = B()

#S = [x*2 for x in range(10)]
#print(S)
