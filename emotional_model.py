import pickle
import os.path

from em_r_novelty import *
from em_relevance import *
from em_implication import *

class Emotion:
    def __init__(self):
        self.load_variables()

        # self.s = Suddenness()
        # self.f = Familiarity()
        # self.p = Predictability()
        self.pl = Pleasantness()
        # self.gr = Goal_Relevance()
        # self.cm = Cause_Motive()
        # self.pr = Probability()
        # self.c = Conduciveness()

    def load_variables(self):
        '''load pickle file with internal variables and store in attribute
        self.internal_variables'''
        if os.path.exists('internal_variables.p'):
            self.internal_variables = pickle.load(open('internal_variables.p','rb'))
        else:
            blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
            universal_variables = {'last_sent': blank_sent,
                                   'delta_sent': blank_sent}
            user_variables = {}
            self.internal_variables = []

    def store_variables(self):
        '''store internal_variables in pickle file'''
        # TODO:  analysis of sent and user
        # store in pickle file
        pickle.dump(self.internal_variables, open('internal_variables.py', 'wb'))

    def code_criteria(self, pos):
        '''Constructs dictionary of emotion critera
        inputs:
            pos: positivity from nltk sentiment analysis,
            float between 0 and 1
        output:
            em_critera: dictionary with critera as keys'''

        # calculate values for critera
        pleasantness = self.pl.calculate(pos)

        # create em_critera dictionary
        self.em_critera = {'pleasantness': pleasantness}

        return self.em_critera

    def interpret(self):
        pass

if __name__ == "__main__":
    model = Emotion()
    em_critera = model.code_criteria(.8)
    print em_critera
