import unittest

class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.thresholds = [.2, .4, .6, .8]
        self.c = Criterium()

    def test_very_low(self):
        pos = self.thresholds[0] - .01
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'very low')

    def test_low(self):
        '''edgecase should round up to low'''
        pos = self.thresholds[0]
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'low')

    def test_medium(self):
        pos = self.thresholds[1]
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'medium')

    def test_high(self):
        pos = self.thresholds[2]
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'high')

    def test_high(self):
        pos = self.thresholds[3]
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'very high')

    # def tearDown(self):
    #     self.thresholds.dispose()
    #     self.c.dispose()


class Criterium:
    def __init__(self, internal_variables, thresholds):
        self.internal_variables = internal_variables
        self.thresholds = thresholds

    def calculate(self, val, thresholds=[.2, .4, .6, .8]):
        # threshold between very low and low
        low_thres = thresholds[0]

        # threshold between low and med
        med_thres = thresholds[1]

        # threshold between med and high
        high_thres = thresholds[2]

        # thresholds between high and very high
        v_high_thres = thresholds[3]

        # returns very low, low, medium, high, or very high
        if val < low_thres:
            return 'very low'
        else:
            if val < med_thres:
                return 'low'
            else:
                if val < high_thres:
                    return 'medium'
                else:
                    if val < v_high_thres:
                        return 'high'
                    else:
                        return 'very high'


if __name__ == "__main__":
    unittest.main()
