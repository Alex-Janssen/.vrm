import sys
import std.vrm_std as vrm

tasks = set([])
lineCharCounts = {}
deferred_tasks = []
trippedFalse = False

context = {
    "types": {},
    "vars": {},
    "funcs": {}
}

vrm.standard_declare(context)

#print("Cur context {} ", context)

def parse(line, context, program, ln):
    #print("Parsing")
    global trippedFalse        
    global lineCharCounts
    #print(line)
    line.strip()
    #print(line)
    tokens = [token.strip() for token in line.split(" ")]

    if trippedFalse:#false if
        #print("tripped false")
        if tokens[-1] == "and" or tokens[-1] == "then":
            return
        if tokens[-1][-1] == ".":
            trippedFalse = False
            return
        if tokens[0] + tokens[1] + tokens[2 ]== "Perchancenotthen":
            trippedFalse = False
            return
        
    if tokens[-1] == "and" or tokens[-1] == "then":
        tokens = tokens[:len(tokens)-1]
    if tokens[-1][-1] == ".":
        tokens[-1] = tokens[-1][:len(tokens[-1])-1]

    if len(tokens) >= 13 and tokens[0]+tokens[1]+tokens[2]+tokens[3] == "Itisknownthat" and tokens[5]+tokens[6]+tokens[7] == "isoftype" and tokens[9]+tokens[10]+tokens[11] == "andofnature":#dec
        #print(tokens[8])
        if tokens[8] in context["types"].keys():
            vals = tokens[12:]
            decVar(tokens[4], context["types"][tokens[8]], vals, context)
        else:
            print("ERROR: Invalid type ", tokens[3])
    if len(tokens) >= 4 and tokens[0]+tokens[1] == "Perchanceis":#if
        if tokens[2].capitalize() in context["funcs"].keys():
            try:
                args = []
                for token in tokens[3:len(tokens)]:
                    if token in context['vars'].keys():
                        args.append(context['vars'][token])
                    else:
                        args.append(decAnonVar(context["types"]["any"], token))
                    #print(args)
                isTrue = context["funcs"][tokens[2].capitalize()].call(args, context)
                #print("Result: ", isTrue)
                if not isTrue:
                    trippedFalse = True
            except:
                print("ERROR: invalid args to function {}.", tokens[2].capitalize())
        else:
            print("ERROR: {} not valid function.", tokens[2].capitalize(), context["funcs"].keys())
    if len(tokens) >= 2 and tokens[0] + tokens[1] == "Perchancenot": #else
        trippedFalse = True
    if tokens[0] in context["funcs"].keys(): #function call
        args = []
        for token in tokens[1:]:
            if token in context['vars'].keys():
                args.append(context['vars'][token])
            else:
                args.append(decAnonVar(context["types"]["any"], token))
            #print(args)
        context["funcs"][tokens[0]].call(args, context)        

    if tokens[0] + tokens[1] == "Ascendto":
        #print("Ascending")
        #print(lineCharCounts)
        #print(tokens)
        program.seek(lineCharCounts[int(tokens[2])-1], 0) 

   # print("Cur context {}", context)


def decVar(name, type, value, context):
    #print(type, value)
    if type.valid(value):
        var = type.declare(value)
        context["vars"][name] = {"value": var, "type": type, "name": name}
        #print("{} of type {} was instantiated to {}", name, type, value)
    else:
        print("INVALID: {} of type {} was NOT instantiated to {}", name, type, value)

def defVar(name, value, vars):
    if name in vars and vars[name]["type"].valid(value):
        vars[name]["value"] = vars[name]["type"].declare(value)

def decAnonVar(type, value):
    #print(type, value)
    if type.valid(value):
        var = type.declare(value)
        res = {"value": var, "type": type}
        #print("Anon: ", res)
        return res
    else:
        print("ERROR: invalid variable, {} of type {} was NOT instantiated to {}", name, type, value)

ln = 0
with open(sys.argv[1], 'r') as program:
    while (cur_line := program.readline()) != "":
        #print(cur_line, len(cur_line))
        if ln != 0: #GOTO
            lineCharCounts[ln+1] = lineCharCounts[ln]+len(cur_line)+1
        else:
            lineCharCounts[0] = 0
            lineCharCounts[ln+1] = len(cur_line)+1
        parse(cur_line, context, program, ln)
        ln+=1