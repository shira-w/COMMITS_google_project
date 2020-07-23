import re
from init import dict_
from init import map_to_main_sub
from init import files
from auto_complete_data import AutoCompleteDataClass

import linecache

#dict={str:str}   dict{regular:str} regular"ab"
def str_to_regular(str): #ba -># b.       dict["ba"]   dict["b."]  startwith
    # regulars=[]
    # for c in str:
    str2 = str.replace(str[-1], '.')
    #t = re.compile(str2)
    return str2


def get_best_k_completions(prefix):
    print(files)
    atoComp=[]
    comp = dict_.get(prefix)
    if comp:
        print("there is comp")
        for c in comp:
            print(files[c[0]])
            print(c[1])
            str_sen=linecache.getline(files[c[0]], c[1])
            print(str_sen)
            #offset=str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, c[0], c[1],1, c[2]))
        return atoComp

    comp2 = dict_.get(map_to_main_sub.get(str_to_regular(prefix)))

    if comp2:
        for c in comp2:
            str_sen = linecache.getline(files[c[0]], c[1])
            #offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, c[0], c[1], 1, c[2]))
        return atoComp
    return None

#print(get_best_k_completions("on"))