class Cell:
    
    def __init__(self, value=None):
        self.values = [value] if value is not None else range(1,10)
        self.options = []
        self.choice = 0
    
    @property
    def value(self):
        if len(self.values) == 1:
            return self.values[0]
        return None
    
    def propagate(self, values):
        if self.value:
            return None # already propagated
        propagated = False
        for value in values:
            if value in self.values:
                self.values.remove(value)
                if len(self.values) == 0:
                    raise Exception("Constraint violation")
                propagated = True
        return propagated

    def set(self, value):
        self.unset()
        if value not in self.values:
            raise Exception("value '%s' not in cell" % self.values)
        self.options = self.values
        self.values = [value]
    
    def unset(self):
        if self.value:
            self.values = self.options
            self.options = []
