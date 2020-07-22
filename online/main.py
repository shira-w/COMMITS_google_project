import re
from auto_complite import get_best_k_completions
from offline.auto_complete_data import AutoCompleteDataClass

#punctuation marks

def input_from_user():
    input_from_user=input("The system is ready. Enter your text")
    while input_from_user!="#":
        ac =get_best_k_completions(input_from_user)
        for i,a in enumerate(ac):
            print(i+". "+ac.completed_sentence)
        input_from_user = input()

completions = get_best_k_completions("This")

print(completions)
for complete in completions:
    print(complete.completed_sentence)
    print(complete.score)
    print(complete.offset)

#why space in print

print("Loading the files and prepariong the system...")


input_from_user()