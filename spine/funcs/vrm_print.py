from spine.funcs.vrm_func import Func
class Print(Func):
    name = "Announce"
    def __init__(self):
        super().__init__(
            self.announce, 
            [{"type": "any"}]
            )
        
    def announce(self, x, context):
        for arg in x:
            print(arg["value"])