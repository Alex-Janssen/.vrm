from spine.types.vrm_type import Type
class vrmNum(Type):
    name = "number"
    def numberValid(self, args):
        if len(args) != 1:
            print("ERROR: number passed in {} args.", len(args))
        try:
            float(args[0])
            return True
        except:
            return False
        
    def defineNumber(self, args):
        return float(args[0])
    
    def __init__(self):
        super().__init__(self.numberValid, self.defineNumber)