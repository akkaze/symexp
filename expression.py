from instruction import *
from variable import Variable
class Expression:
    def __init__(self,rhs):
        self._rhs = rhs
        self._lhs = Variable(name = '')
    @property
    def lhs(self):
        return self._lhs
class Alloc(Expression):
    def __init__(self,rhs):
        Expression.__init__(self,rhs)
        AllocInstr(rhs = self._rhs,lhs = self._lhs)
    def to_var(self):
        return self._rhs
class Plus(Expression):
    def __init__(self,rhs):
        Expression.__init__(self,rhs)
        for rhs in self._rhs:
            self._lhs.children.append(rhs)
        PlusOp(rhs = self._rhs,lhs = self._lhs)
    def to_var(self):
        return self._lhs
class Mul(Expression):
    def __init__(self,rhs):
        Expression.__init__(self,rhs)
        for rhs in self._rhs:
            self._lhs.children.append(rhs)
        MulOp(rhs = self._rhs,lhs = self._lhs)
    def to_var(self):
        return self._lhs