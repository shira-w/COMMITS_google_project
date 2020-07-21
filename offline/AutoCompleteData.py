#file

#@dataclass
class AutoCompleteDataClass:

    def __init__(self,completed_sentence,source_text,offset,score):
        self.completed_sentence=completed_sentence #str
        self.source_text=source_text #str
        self.offset=offset #int
        self.score=score #int
    # methods that you need to define by yourself
