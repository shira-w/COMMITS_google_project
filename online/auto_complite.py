import re
from offline.init import dict_
from offline.init import map_to_main_sub

def str_to_regular(str):
    #regulars=[]
    #for c in str:
    str2=str.replace(str[-1],'.')
    #t = re.compile(str2)
    return str2

def get_best_k_completions(prefix):
    comp=dict_.get(prefix)
    if(comp!=None):
        return comp

    comp2=dict_.get(map_to_main_sub.get(str_to_regular(prefix)))
    if (comp2!=None):
        return comp2
    return None


print(get_best_k_completions("to bi"))

