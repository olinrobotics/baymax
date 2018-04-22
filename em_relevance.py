from em_criterium import *

class Pleasantness(Criterium):
    def __init__(self):
        pass

    def code(self):
        pass


class Goal_Relevance(Criterium):
    def code(self):
        return 'high'

    def interpret(self, criterum_state, possible_em):
        '''takes the argument criterum_state a list of current possible emotions
        and returns which of those are possible given the criterium state'''

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
