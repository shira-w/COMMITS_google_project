import json
import os
from os import walk
from os.path import join
import string
import re
from json.decoder import JSONDecodeError

from auto_complete_data import AutoCompleteDataClass

map_to_main_sub = {}
files = []

def str_to_regular(str,i):
    str2=str[:i]+'.'+str[i+1:]
    return str2

def sub_strings(line):
    sub_str = []
    line = "".join(re.split("[^a-zA-Z0-9]*", line))
    line = line.casefold()  # ------------אולי מיותר ה = --------------------
    len_ = len(line)
    for i in range(1, len_):
        for j in range(i + 1, min(len_, i + 12)):
            sub_str.append(line[i:j])  # ----לשנות שיהיה את כל תתי מחרוזות ולא רק תחיליות בגבול מסוים------
            for y in range(1, len(line[i:j])):
                str2=str_to_regular(line[i:j], y)
                sub_str.append(str2)

    return sub_str

#shura 21
#girsa not aarrang
"""
def sub_strings(line):
    list = []
    for i in range(1, len(line)//2):
        print(i)
        list.append(line[0:i])
    return list"""


def read_from_file(file):
    print(file)
    print(files)
    index_file = len(files) - 1

    for index_line, line in enumerate(file):
        # print(index_line)
        if line.strip():
            # print(line)
            substring = sub_strings(line)
            print(substring)
            # print(substring)
            # index_line=index_line+1
            for x in substring:
                score = len(x) * 2
                data = [index_file, index_line + 1, score]
                json_name=x[0]+".json"
                #send to func?
                kash = [{}]

                #if os.path.exists(json_name):
                print(json_name)
                with open(json_name)as f:   #why if empty?
                    #if(json.load(f)):
                    print(json.load)
                    try:
                        kash = json.load(f)#cache
                    except JSONDecodeError:
                        pass


                if kash[0].get(x):
                    if len(kash[0][x]) == 5:
                            pass

                    else:
                        kash[0][x].append(data)

                else:
                    kash[0][x] = [data]

                with open(json_name,"w") as f:
                    json.dump(kash,f)   #what is indent 4?

    # else:
    # index_line=index_line-1

def read_root(root_name):
    for root_name, dirs, files_name in os.walk(root_name):
        for file in files_name:
            with open(os.path.join(root_name, file), "r", encoding='utf8') as auto:
                files.append(auto.name)
                read_from_file(auto)
            # queries = read_file(os.path.join(root, file))
    # print(queries)


def from_key_to_regulars(key):
    regulars = []
    for k in key:
        regulars.append(key.replace(k, '.'))
    return regulars


def init_map_to_main_sub():  # student   .tduent s.udde
    for k in dict_.keys():
        # print(k)
        # if len(k)!= 1 and (k[1] != " " or len(k) != 2):
        for reg in from_key_to_regulars(k):
            map_to_main_sub[reg] = k


read_root("technology_texts")
#init_map_to_main_sub()
