from spine.funcs.vrm_func import Func
class Augment(Func):
    name = "Augment"
    def augment(self, x, context):
                if len(x) > 1:
                      print("Too many variables in augment: {}.", len(x))
                if x[0]['name'] not in context["vars"].keys():
                    print("Error: variable {} unknown.", x)
                context['vars'][x[0]['name']]["value"] += 1
    def __init__(self):
        super().__init__(
            self.augment,
            [{"type": "number"}]
            )