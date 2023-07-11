class Type:
    def __init__(self, isValid, define):
        self.isValid = isValid
        self.define = define
    
    def valid(self, value):
        return self.isValid(value)
    
    def declare(self, value):
        return self.define(value)