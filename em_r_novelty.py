from em_criterium import *

class Novelty(Criterium):
    def __init__(self):
        pass

    def code(self):
        pass


class Suddenness(Criterium):
    def code(self):
        # defines last compound score
        last_compound = self.internal_variables[0]['last_sent']['compound']
        print 'last: ', last_compound
        # defines current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']
        print 'current: ', current_compound
        # defines change, suddenness uses absolute value of difference
        delta_compound = abs(last_compound - current_compound)
        print 'delta: ', delta_compound 

        # calculate suddenness as very low, low, medium, high, or very high
        suddenness = self.calculate(delta_compound, self.thresholds)
        return suddenness


class Familiarity(Criterium):
    def code(self):
        pass


class Predictability(Criterium):
    def code(self):
        pass
