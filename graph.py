from node import *
class Graph:
    def __init__(self, **kwargs):
        self._instrs = []
        self._vars = []
    @property
    def nodes(self):
        return self._nodes
    @property
    def vars(self):
        return self._vars
    @property
    def instrs(self):
        return self._instrs
    def add_instr(self,instr):
        self._instrs.append(instr)
    def add_var(self,var):
        self._vars.append(var)
    def presort_nodes2(self):
        from instruction import AllocInstr
        n_nodes = len(self._nodes)
        for i in range(n_nodes):
            self._node2children[i] = []
        for i in range(n_nodes):
            for j in range(n_nodes):
                if i is j:
                    pass
                elif isinstance(self._nodes[i].instr,AllocInstr):
                    pass
                elif self._nodes[j].instr.lhs_name in self._nodes[i].instr.rhs_names:
                    self._node2children[j].append(i)
    def presort_nodes(self):
        n_nodes = len(self._nodes)
        for i in range(n_nodes):
            self._node2children[i] = []
        for i in range(n_nodes):
            for j in range(n_nodes):
                if i is j:
                    pass
                elif self._nodes[i].instr.lhs in self._nodes[j].instr.lhs.children:
                    self._node2children[j].append(i)
    def topsort_nodes(self):
        n_nodes = len(self._nodes)
        in_degrees = [0] * n_nodes
        for i in range(n_nodes):
            for j in self._node2children[i]:
                in_degrees[j] = in_degrees[j] + 1
        for i in range(n_nodes):
            for j in range(n_nodes):
                if j in self._topsorted_idxes:
                    pass
                elif in_degrees[j] is 0:
                    self._topsorted_idxes.append(j)
                    for k in range(n_nodes):
                        if k in self._node2children[i]:
                            in_degrees[k] = in_degrees[k] - 1
                    break 

    def run(self):
        self._nodes = [Node(instr = instr) for instr in self._instrs] 
        self._topsorted_idxes = []
        self._node2children = dict()
        self.presort_nodes()
        self.topsort_nodes()
        for idx in self._topsorted_idxes:
            self._nodes[idx].instr.run()
            print self._nodes[idx].instr.lhs.name
            for var in self._vars:
                print  var.ref_count,
            print