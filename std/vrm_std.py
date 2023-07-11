import spine.types.vrm_num as number
import spine.types.vrm_any as any

import spine.funcs.vrm_augment as augment
import spine.funcs.vrm_less as smaller 
import spine.funcs.vrm_print as print

def standard_declare(context):
    declare_types(context)
    declare_funcs(context)

def declare_types(context):
    context["types"][number.vrmNum.name] = number.vrmNum()
    context["types"][any.vrmAny.name] = any.vrmAny()

def declare_funcs(context):
    context["funcs"][augment.Augment.name] = augment.Augment()
    context["funcs"][print.Print.name] = print.Print()
    context["funcs"][smaller.Smaller.name] = smaller.Smaller()