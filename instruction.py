from config import g
class Instruction:
    def __init__(self,**kwargs):
        g.add_instr(self)
        self._lhs = kwargs['lhs']
        self._rhs = kwargs['rhs']
        self._lhs_name = self._lhs.name
        
    def run(self):
        pass
class AllocInstr(Instruction):
    def __init__(self,**kwargs):
        Instruction.__init__(self,**kwargs)
    def run(self):
        Instruction.run(self)
        self._lhs.data = self._rhs
    @property
    def lhs(self):
        return self._lhs
    @property
    def lhs_name(self):
        return self._lhs_name
class Operation(Instruction):
    def __init__(self,**kwargs):
        Instruction.__init__(self,**kwargs)
        for rhs in self._rhs:
            rhs.ref_count = rhs.ref_count + 1
        self._rhs_names = []
        for rhs in self._rhs:
            self._rhs_names.append(rhs.name)
    @property
    def lhs(self):
        return self._lhs
    @property
    def rhs(self):
        return self._rhs
    @property
    def lhs_name(self):
        return self._lhs_name
    @property
    def rhs_names(self):
        return self._rhs_names
        
    def run(self):
        Instruction.run(self)
        for rhs in self._rhs:
            rhs.ref_count = rhs.ref_count - 1
        return
class PlusOp(Operation):
    def __init__(self, **kwargs):
        if len(kwargs['rhs']) is not 2:
            raise RuntimeError('')
        Operation.__init__(self,**kwargs)
    def run(self):
        Operation.run(self)
        self._lhs.data = self._rhs[0].data + self._rhs[1].data
class MulOp(Operation):
    def __init__(self, **kwargs):
        if len(kwargs['rhs']) is not 2:
            raise RuntimeError('')
        Operation.__init__(self,**kwargs)
    def run(self):
        Operation.run(self)
        self._lhs.data = self._rhs[0].data * self._rhs[1].data