from offline.auto_complete_data import AutoCompleteDataClass

dict_={}
map_to_main_sub={}

def sub_strings(line):
    list=[]
    for i in range(1,len(line)):
        list.append(line[:i])

    return list

def read_from_file(name):
    f = open(name, "r")
    with open(name) as file_in:
        for line in file_in:
            print(line)
            substring = sub_strings(line)
            i=1
            for x in substring:
                score = len(x) * 2
                if(dict_.get(x)!=None):
                    #fix it!
                    if len(dict_[x])==5:
                        j=4
                        data=AutoCompleteDataClass(line, name, i, score)
                        while j>-1:
                            if dict_[x][j].score < score:
                                dict_[x][j+1]=dict_[x][j]
                                dict_[x][j]=data
                            else:
                                break

                            j=j-1

                    else:
                        dict_[x].append(AutoCompleteDataClass(line,name,i,score))

                else:
                    dict_[x]=[AutoCompleteDataClass(line,name,i,score)]
    return dict_

def from_key_to_regulars(key):
    regulars=[]
    for k in key:
        regulars.append(key.replace(k,'.'))
    return regulars


def init_map_to_main_sub():
    for k in dict_.keys():
        if len(k) != 1 and (k[1]!=" " or len(k)!=2):
            for reg in from_key_to_regulars(k):
                map_to_main_sub[reg]=k



print(read_from_file("check.txt"))
print(dict_.keys())

init_map_to_main_sub()

print(map_to_main_sub)


