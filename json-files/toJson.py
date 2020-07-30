import json

def read_root(root_name):
    for root_name, dirs, files_name in os.walk(root_name):
        for file in files_name:
            with open(os.path.join(root_name, file),"r", encoding='utf8') as auto:
                files.append(auto.name)
                read_from_file(auto)

def fromTextTojson(file):
    data={"kk":4,"ppp":9}
    with open("c.json")as f:
        r=json.load(f)
    print(r)
    #with open("data.json", 'a+') as f:
        #json.dump(data, f)



fromTextTojson("check.txt")