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

    def interpret(self):
        '''takes the argument criterum_state a list of current possible emotions
        and returns which of those are possible given the criterium state'''
        independent_emotions = ['DISP/DISG', 'CON/SCO', 'GUIlT', 'PRIDE']
        switcher = {
            'very low': [],
            'low': ['DISP/DISG', 'CON/SCO', 'BOR/IND'],
            'medium': ['ENJ/HAP', 'ANX/WOR', 'IRR/COA'],
            'high': ['ELA/JOY', 'SAD/DEJ', 'DESPAIR', 'FEAR', 'RAG/HOA',
                     'SHAME', 'GUILT', 'PRIDE'],
            'very high': []
        }
        all_possible = switcher.get(criterum_state)

        return self.downselect(possible_em, all_possible)

class Urgency:
    def __init__(self):
        pass

    def code(self):
        pass
