from config import g
class Variable:
    def __init__(self, *args,**kwargs):
        #from expression import Expression
        #if len(args) is not 0:
        #    if isinstance(args[0],Variable):
        #        self._ref_count = args[0].ref_count
        #        self.data = args[0].data
        #        self.children = args[0].children
        #    if isinstance(args[0],Expression):
        #        self._ref_count = args[0].rhs.ref_count
        #        self.data = args[0].rhs.data
        #        self.children = args[0].rhs.children
        #elif len(kwargs) is not 0:
            self._name = kwargs['name']
            self._ref_count = 0
            self._data = 0
            self._children = []
        
    @property
    def name(self):
        return self._name
    @property
    def ref_count(self):
        return self._ref_count
    @property
    def data(self):
        return self._data
    @property
    def children(self):
        return self._children
def assign(var,exp):
    if isinstance(exp.lhs,Variable):
        var.ref_count = exp.lhs.ref_count
        var.data = exp.lhs.data
        var.children = exp.lhs.children