class Func:
    def __init__(self, function, params):
        self.function = function
        self.params = params

    def canCall(self, argList):
        #print(len(argList))
        #print(len(self.params))
        for ind, arg in enumerate(argList):
            if self.params[ind]['type'] == 'any':
                continue
            if(self.params[ind]['type'] != arg["type"].name):
                print("Warning: Invalid call for {}, expected {} but got {}.", self.name, self.params[ind]["type"], arg["type"].name)
                return False
        #print("Valid call")
        return True
    
    def call(self, argList, context):
        #print("Called")
        if self.canCall(argList):
            #print("Calling")
            return self.function(argList, context)