from em_criterium import *

class Novelty(Criterium):
    def __init__(self):
        pass

    def code(self):
        pass


class Suddenness(Criterium):
    # def __init__(self, internal_variables, thresholds):
    #     pass

    def code(self):
        # defines last compound score
        last_compound = self.internal_variables[0]['last_sent']['compound']
        # defines current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']
        # defines change, suddenness uses absolute value of difference
        delta_compound = abs(last_compound - current_compound)

        # calculate suddenness as very low, low, medium, high, or very high
        suddenness = self.calculate(delta_compound, self.thresholds)
        return suddenness


class Familiarity(Criterium):
    def __init__(self):
        pass

    def code(self):
        pass


class Predictability(Criterium):
    def __init__(self):
        pass

    def code(self):
        pass
