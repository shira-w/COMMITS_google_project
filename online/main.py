import re
from auto_complite import get_best_k_completions

#simaney pisuk



#t = re.compile(r't. be or n')
a = get_best_k_completions("i am")

for i in a:
    print(i.completed_sentence)
    print(i.score)
    print(i.offset)

