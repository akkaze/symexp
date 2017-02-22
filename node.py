class Node:
    def __init__(self, **kwargs):
        self._instr = kwargs['instr']
        self._children = []
    @property
    def instr(self):
        return self._instr