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
        self.blank_variables = {'current_sent': self.blank_sent,
                                'last_sent': self.blank_sent,
                                'delta_sent': self.blank_sent,
                                'average_sent': self.blank_sent,
                                'average_delta': self.blank_sent,
                                'num_data': 0}
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
        self.load_pickle_file()
        self.add_universal_variables()
        self.add_user_variables()
        print self.internal_variables

    def load_pickle_file(self):
        # Load variables
        if os.path.exists('internal_variables.p'):
            self.internal_variables = pickle.load(open('internal_variables.p','rb'))
        else:
            universal_variables = self.blank_variables
            user_variables = {}
            self.internal_variables = [universal_variables, user_variables]

    def store_pickle_file(self):
        '''store internal_variables in pickle file'''
        # TODO:  analysis of sent and user
        # store in pickle file
        self.add_variables_end(self.internal_variables[0])
        self.add_variables_end(self.internal_variables[1][self.user_name])
        pickle.dump(self.internal_variables, open('internal_variables.py', 'wb'))

    def add_universal_variables(self):
        # update universal_variables
        universal_variables = self.internal_variables[0]

        universal_variables['current_sent'] = self.user_sent
        universal_variables['num_data'] += 1

        # update average sentiment
        current = universal_variables['current_sent']
        average = universal_variables['average_sent']
        num = universal_variables['num_data']
        universal_variables['average_sent'] = self.average_sent(current,
                                                                average, num)
        self.internal_variables[0] = universal_variables

    def add_user_variables(self):
        overwrite = False
        # check if user is in database, if not, make new user
        if self.user_name not in self.internal_variables[1] or overwrite:
            self.internal_variables[1][self.user_name] = self.blank_variables

        # update user variables
        user_variables = self.internal_variables[1][self.user_name]

        user_variables['current_sent'] = self.user_sent
        user_variables['num_data'] += 1

        # update average sentiment
        user_variables['average_sent'] = self.average_sent(user_variables['current_sent'],
                                                           user_variables['average_sent'],
                                                           user_variables['num_data'])

        self.internal_variables[1][self.user_name] = user_variables

    def add_variables_end(self, variable_dict):
        '''modifies variable_dict as necessary before storing
            - stores difference between current_sent and last_sent as delta_sent
            - stores current_sent as last_sent
            - changes current_sent to blank_sent
            - update average_delta
        '''
        # store difference between current_sent and last_sent
        variable_dict['delta_sent'] = self.diff_sent(variable_dict['current_sent'],
                                                     variable_dict['last_sent'])

        # store current_sent as last_sent
        variable_dict['last_sent'] = variable_dict['current_sent']

        # changes current_sent to blank_sent
        variable_dict['current_sent'] = self.blank_sent

        # update average_delta
        self.average_sent(variable_dict['delta_sent'],
                          variable_dict['average_delta'],
                          variable_dict['num_data'] - 1)

    def average_sent(self, current, average, num_data):
        '''Updates the average_sent given variable_dict'''
        # TODO: change the parameters to two sentiment dictionaries?
        average['pos'] = (average['pos'] + current['pos'])/num_data

        average['neg'] = (average['neg'] + current['neg'])/num_data

        average['neu'] = (average['neu'] + average['neu'])/num_data

        average['compound'] = (average['compound'] +
                               current['compound'])/num_data

        return average

    def diff_sent(self, current_sent, last_sent):
        '''Takes difference of two different sentiment dictionaries'''
        diff = {}
        diff['pos'] = last_sent['pos'] - current_sent['pos']
        diff['neg'] = last_sent['neg'] - current_sent['neg']
        diff['neu'] = last_sent['neu'] - current_sent['neu']
        diff['compound'] = last_sent['compound'] - current_sent['compound']
        return diff

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

        # store internal_variables in pickle file
        model.store_pickle_file()

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

    print em_critera
