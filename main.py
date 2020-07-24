import re
import string
from auto_complite import get_best_k_completions
from auto_complete_data import AutoCompleteDataClass


def input_from_user():
    input_from_user_ = input("The system is ready. Enter your text:")
    input_from_user_add = ""
    while input_from_user_ != "exit from google":
        if input_from_user_add == "#":
            input_from_user_add = ""
            input_from_user_ = input("Enter your text again:")

        while input_from_user_ != "#" and input_from_user_add != "#":
            input_from_user_ = input_from_user_.casefold()
            input_from_user_ = input_from_user_.strip()
            input_from_user_.translate(str.maketrans('', '', string.punctuation))

            ac = get_best_k_completions(input_from_user_)
            if ac:
                for i, a in enumerate(ac):
                    #miyun lefi ofset
                    print(str(i + 1) + ". " + a.completed_sentence + " (" + a.source_text + " " + str(a.source_line) + ") score:"+str(a.score))
            if input_from_user_ == "exit from google":
                break
            else:
                print("search online...")
            # input_from_user =input_from_user+input("add")
            input_from_user_add = input(input_from_user_)
            input_from_user_ = input_from_user_ + input_from_user_add
            #print(input_from_user_)


# completions = get_best_k_completions("This")

# print(completions)
# for complete in completions:
# print(complete.completed_sentence)
# print(complete.score)
# print(complete.offset)

# why space in print

print("Loading the files and prepariong the system...")
input_from_user()

# input_from_user()
