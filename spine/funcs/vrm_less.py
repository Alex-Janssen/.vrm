from spine.funcs.vrm_func import Func
class Smaller(Func):
    name = "Smaller"
    def less_than(self, arg_list, context):
        if(len(arg_list) != 3):
            print("Error, expected arg list of length 3 for smaller, got {}", arg_list)
            return False
        if arg_list[1]['value'] != "than":
            print("Error, expected than for smaller, got {}.", arg_list[1])
        return arg_list[0]["value"] < arg_list[2]["value"]

    def __init__(self):
        super().__init__(
            self.less_than,
            [{"type": "number"}, {"type": "any"}, {"type": "number"}]
            )