from variable import *
from instruction import AllocInstr,PlusOp,MulOp
from graph import Graph
from expression import *
from config import g
a = Variable(name = 'a')
g.add_var(a)
b = Variable(name = 'b')
g.add_var(b)
c = Variable(name = 'c')
g.add_var(c)
d = Variable(name = 'd')
g.add_var(d)
e = Variable(name = 'e')
g.add_var(e)
e1= Alloc(1.)
assign(a,e1)
e2 = Alloc(2.)
assign(b,e2)
e3 = Plus([a,b])
assign(c , e3)
e4 = Mul([a,c])
assign(d, e4)
e5 = Mul([c,d])
assign(e,e5)
g.run()
print e.data