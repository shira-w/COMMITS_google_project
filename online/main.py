import re
import string
from auto_complite import get_best_k_completions
from auto_complete_data import AutoCompleteDataClass

#score
#for for all
#One  in them in the tat ignore and spacec aqt
#hosafa hachsara
#'#'
#hadpasot vehearot

def input_from_user():
    input_from_user=input("The system is ready. Enter your text:")
    #while(input_from_user!="exit from google"):

    while(input_from_user!="exit from google"):
        #input_from_user=""
        while input_from_user!="#":
            input_from_user=input_from_user.casefold()
            input_from_user=input_from_user.strip()
            #what about on,e not good!
            input_from_user.translate(str.maketrans('', '', string.punctuation))

            ac =get_best_k_completions(input_from_user)
            if ac:
                for i,a in enumerate(ac):
                    print(str(i+1)+". "+a.completed_sentence)
            else:
                print("search online...")
            #input_from_user =input_from_user+input("add")
            input_from_user=input("add")





#completions = get_best_k_completions("This")

#print(completions)
#for complete in completions:
    #print(complete.completed_sentence)
    #print(complete.score)
    #print(complete.offset)

#why space in print

print("Loading the files and prepariong the system...")
input_from_user()

#input_from_user()
