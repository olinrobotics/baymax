from em_r_novelty import *
from em_relevance import *
from em_implication import *

class Emotion:
    def __init__(self):
        self.s = Suddenness()
        self.f = Familiarity()
        self.p = Predictability()
        self.pl = Pleasantness()
        self.gr = Goal_Relevance()
        self.cm = Cause_Motive()
        self.pr = Probability()
        self.c = Conduciveness()

    def code(self):
        pass

    def interpret(self):
        pass

if __name__ = "__main__":
    model = Emotion()
