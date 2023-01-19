from prototype.prototype import Protoype
from copy import deepcopy


class Concrete(Protoype):
    
    def clone(self): return deepcopy(self)
