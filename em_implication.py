from em_criterium import *

class Cause_Motive:
    def __init__(self):
        pass

    def code(self):
        pass


class Probability:
    def __init__(self):
        pass

    def code(self):
        pass


class Conduciveness(Criterium):
    def code(self):
        # defines current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']

        # calculates conduciveness as very low, low, medium, high, or very high
        conduciveness = self.calculate(current_compound, self.thresholds)

        return conduciveness

class Urgency:
    def __init__(self):
        pass

    def code(self):
        pass
