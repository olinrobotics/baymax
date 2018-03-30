from em_r_novelty import *

class Pleasantness:
    def __init__(self):
        pass

    def calculate(self, pos):
        # threshold between very low and low
        low_thres = .25
        # threshold between low and high
        thres = .5.
        # threshold between high and very high
        high_thres
        if pos >= thres:
            if pos >= high_thres:
                return 'very high'
            else:
                return 'high'
        elif pos < thres:
            if pos >= low_thres:
                return 'low'
            else:
                return 'very low'
        return pleasantness


class Goal_Relevance:
    def __init__(self):
        pass

    def code(self, em_profile):
        pass
