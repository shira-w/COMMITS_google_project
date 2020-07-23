import re
from init import dict_
from init import map_to_main_sub
from init import files
from auto_complete_data import AutoCompleteDataClass

import linecache


#dict={str:str}   dict{regular:str} regular"ab"
def str_to_regular(str,i): #ba -># b.       dict["ba"]   dict["b."]  startwith
    #regulars=[]
    #for i in range(1,len(str)+1):
    #str2 = str[:i]+'.'+str[i:]   add function!!!
    str2=str[:i]+'.'+str[i+1:]
        #regulars.append(str2)
    #t = re.compile(str2)
    return str2

#print(str_to_regular("ac"))

def get_best_k_completions(prefix):
    print(files)
    atoComp=[]
    comp = dict_.get(prefix)
    if comp:
        for c in comp:
            str_sen=linecache.getline(files[c[0]], c[1])

            #offset=str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, files[c[0]], c[1],1, c[2]))
        return atoComp
    end=-1*len(prefix)
    i=-1
    if i!=end:
        comp2 = dict_.get(map_to_main_sub.get(str_to_regular(prefix,i)))
    else:
        return None
    if comp2:
        for c in comp2:
            str_sen = linecache.getline(files[c[0]], c[1])
            #offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, c[2]))
        return atoComp

    i=i-1
    if i!=end:
        comp3= dict_.get(map_to_main_sub.get(str_to_regular(prefix,i)))
    else:
        return None

    if comp3:
        for c in comp3:
            str_sen = linecache.getline(files[c[0]], c[1])
            #offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, c[2]))
        return atoComp

    i = i - 1
    if i!=end:
        comp4= dict_.get(map_to_main_sub.get(str_to_regular(prefix,i)))
    else:
        return None

    if comp4:
        for c in comp3:
            str_sen = linecache.getline(files[c[0]], c[1])
            #offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, c[2]))
        return atoComp

    i = i - 1
    if i != end:
        comp5 = dict_.get(map_to_main_sub.get(str_to_regular(prefix, i)))
    else:
        return None
    if comp5:
        for c in comp5:
            str_sen = linecache.getline(files[c[0]], c[1])
            #offset = str_sen.index(prefix)
            atoComp.append(AutoCompleteDataClass(str_sen, files[c[0]], c[1], 1, c[2]))
        return atoComp

    return None

