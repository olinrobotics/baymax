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

        # defines current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']

        # defines change, suddenness uses absolute value of difference
        delta_compound = abs(last_compound - current_compound)

        # calculate suddenness as very low, low, medium, high, or very high
        suddenness = self.calculate(delta_compound, self.thresholds)

        return suddenness

    def interpret(self, criterum_state, possible_em):
        '''takes the argument criterum_state a list of current possible emotions
        and returns which of those are possible'''
        # emotions that doesn't change based on suddenness
        independent_emotions = ['DISP/DISG', 'CON/SCO', 'GUIlT', 'PRIDE']
        switcher = {
            'very low': ['BOR/IND'],
            'low': ['ENJ/HAP', 'SAD/DEJ', 'ANX/WOR', 'IRR/COA', 'SHAME'],
            'medium': ['ELA/JOY'],
            'high': ['ELA/JOY', 'DESPAIR', 'FEAR', 'RAG/HOA'],
            'very high': []
        }
        all_possible = switcher.get(criterum_state) + independent_emotions

        return self.downselect(possible_em, all_possible)


class Familiarity(Criterium):
    def __init__(self, internal_variables, thresholds):
        self.internal_variables = internal_variables
        self.thresholds = thresholds

    def code(self):
        # define average compound score
        average_compound = self.internal_variables[0]['average_sent']['compound']

        # define current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']

        # define change as absolute value of difference
        delta_compound = abs(average_compound - current_compound)

        # calculate familiarity as very low, low, medium, high, or very high
        familiarity = self.reverse_calculate(delta_compound, self.thresholds)

        return familiarity


class Predictability(Criterium):
    def __init__(self, internal_variables, thresholds, user_name):
        self.internal_variables = internal_variables
        self.thresholds = thresholds
        self.user_name = user_name

    def code(self):
        # define average compound score for user
        average_compound = self.internal_variables[1][self.user_name]['average_sent']['compound']

        # define current compound score
        current_compound = self.internal_variables[0]['current_sent']['compound']

        # defines change as absolute value of difference
        delta_compound = abs(average_compound - current_compound)

        # calculate predictability as very low, low, medium, high, or very high
        predictability = self.reverse_calculate(delta_compound, self.thresholds)

        return predictability
