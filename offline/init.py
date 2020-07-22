import os
from os import walk
from os.path import join

# class names
from offline.auto_complete_data import AutoCompleteDataClass

dict_ = {}
map_to_main_sub = {}  #studen.? #stude.t
files = []
"""
def read_file(file_name):
    with open(file_name, 'r') as the_file:
        return the_file.read().split("\n")"""


def read_from_file(file):
    # f = open(name, "r")
    print(file)

    #with open(name,"r") as file_in:
    index_file = len(files) - 1
        # for line,index

    for index_line, line in enumerate(file):
        substring = sub_strings(line)
    # index_line=index_line+1
        i = 1
        for x in substring:
            score = len(x) * 2
            data = [index_file, index_line, score]

            if dict_.get(x):
                # fix it!
                if len(dict_[x]) == 5:
                    j = 4
                    # data=AutoCompleteDataClass(line, name, i, score)
                    while j > -1:
                        if dict_[x][j][2]< score:
                            dict_[x][j + 1] = dict_[x][j]
                            dict_[x][j] = data
                        else:
                            break

                        j = j - 1

                    else:
                        dict_[x].append(data)

            else:
                dict_[x] = [data]

def read_root(root_name):
    for root_name, dirs, files_name in os.walk(root_name):
        for file in files_name:
            files.append(file)
            with open(os.path.join(root_name, file),"r", encoding='utf8') as auto:
                read_from_file(auto)
            # queries = read_file(os.path.join(root, file))
    # print(queries)


def sub_strings(line):
    list = []
    for i in range(1, len(line)):
        list.append(line[:i])

    return list


def from_key_to_regulars(key):
    regulars = []
    for k in key:
        regulars.append(key.replace(k, '.'))
    return regulars


def init_map_to_main_sub(): #student   .tduent s.udde
    for k in dict_.keys():
        if len(k) != 1 and (k[1] != " " or len(k) != 2):
            for reg in from_key_to_regulars(k):
                map_to_main_sub[reg] = k



read_root("root")
#read_from_file("check.txt")

init_map_to_main_sub()

#print(map_to_main_sub)

#dic ax a. .x i efshar   -> im mavirim lekvatsim   a b c    abba=["abbakjkjk"]   dic zmani
# im shelanu regular cmo sheze achashav bli hachlafot   -> hachlafot>>file
#generiyut
#map["ax"]=["a.",".x"]
# im ani mavira et hanekodot: ani lo yodaat dic      al   nekudot
#clali -> prati modolari files dic kash json !!!!!!!!! toanim ledic
#kash -> popolarim milim shlemot
#  "a"

#int er psikim
#substrung lehitalem
#kriaa mekovets