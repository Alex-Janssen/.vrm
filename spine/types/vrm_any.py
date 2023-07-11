from spine.types.vrm_type import Type
class vrmAny(Type):
    name = "any"
    def numberValid(self, value):
        return True
        
    def defineAny(self, value):
        return value
    
    def __init__(self):
        super().__init__(self.numberValid, self.defineAny)