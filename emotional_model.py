import pickle
import os.path

from em_r_novelty import *
from em_relevance import *
from em_implication import *

class Emotion:
    def __init__(self, user_name, user_sent):
        self.user_name = user_name
        self.user_sent = user_sent

        self.blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
        # note: delta_sent is last delta_sent, new one will have to be calculated
        self.blank_variables = {'current_sent': self.user_sent,
                                'last_sent': self.blank_sent,
                                'delta_sent': self.blank_sent,
                                'average_sent': self.blank_sent,
                                'average_delta': self.blank_sent}
        self.load_variables()

        default_thres = [.2, .4, .6, .8]
        self.thresholds = {'suddenness': default_thres}

        self.s = Suddenness(self.internal_variables, self.thresholds['suddenness'])
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
        # Load variables
        if os.path.exists('internal_variables.p'):
            self.internal_variables = pickle.load(open('internal_variables.p','rb'))
        else:
            universal_variables = self.blank_variables
            user_variables = {}
            self.internal_variables = [universal_variables, user_variables]

        # add current variables to internal_variables
        self.internal_variables[0]['current_sent'] = self.user_sent
        # check if user is in database, if not, make new user
        if self.user_name in self.internal_variables[1]:
            self.internal_variables[1][self.user_name]['current_sent'] = self.user_sent
        else:
            self.internal_variables[1][self.user_name] = self.blank_variables

    def store_variables(self):
        '''store internal_variables in pickle file'''
        # TODO:  analysis of sent and user
        # store in pickle file
        pickle.dump(self.internal_variables, open('internal_variables.py', 'wb'))

    def code_criteria(self):
        '''Constructs dictionary of emotion critera
        inputs:
            pos: positivity from nltk sentiment analysis,
            float between 0 and 1
        output:
            em_critera: dictionary with critera as keys'''

        # calculate values for critera
        suddenness = self.s.code()

        # create em_critera dictionary
        self.em_critera = {'suddenness': suddenness}

        return self.em_critera

    def interpret(self):
        pass

if __name__ == "__main__":
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    print "Hello, I'm Baymax, your personal healthcare companion"

    # Ask the patient for their name
    patient_name = raw_input("Who are you? ")
    print "Hello, %s!" % patient_name

    # Ask the patient how they are
    patient_status = raw_input("How are you today? ")
    print patient_status

    # Sentiment analysis proof of concept
    sid = SentimentIntensityAnalyzer()
    patient_sentiment = sid.polarity_scores(patient_status)

    model = Emotion(patient_name, patient_sentiment)
    em_critera = model.code_criteria()
    print model.internal_variables
    print em_critera
