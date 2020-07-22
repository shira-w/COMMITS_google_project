import re
from offline.init import dict_
from offline.init import map_to_main_sub
from offline.init import files
import linecache


#dict={str:str}   dict{regular:str} regular"ab"
def str_to_regular(str): #ba -># b.       dict["ba"]   dict["b."]  startwith
    # regulars=[]
    # for c in str:
    str2 = str.replace(str[-1], '.')
    #t = re.compile(str2)
    return str2


def get_best_k_completions(prefix):
    atoComp=[]
    comp = dict_.get(prefix)
    if comp:
        print("there is comp")
        for c in comp:
            str_sen=linecache.getline(files[c[0]], files[c[1]])
            offset=str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, c[0], c[1],offset, c[2]))
        return atoComp

    comp2 = dict_.get(map_to_main_sub.get(str_to_regular(prefix)))

    if comp2:
        for c in comp2:
            str_sen = linecache.getline(files[c[0]], files[c[1]])
            offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, c[0], c[1], offset, c[2]))
        return atoComp
    return None
