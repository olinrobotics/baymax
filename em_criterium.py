import unittest

class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.thresholds = [.2, .4, .6, .8]
        self.blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
        # note: delta_sent is last delta_sent, new one will have to be calculated
        self.internal_variables = {'current_sent': self.blank_sent,
                                'last_sent': self.blank_sent,
                                'delta_sent': self.blank_sent,
                                'average_sent': self.blank_sent,
                                'average_delta': self.blank_sent,
                                'num_data': 0}
        self.c = Criterium(self.internal_variables, self.thresholds)

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

    def test_very_high(self):
        pos = self.thresholds[3]
        calculation = self.c.calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'very high')

    # def tearDown(self):
    #     self.thresholds.dispose()
    #     self.c.dispose

class TestReverseCalculation(unittest.TestCase):
    def setUp(self):
        self.thresholds = [.2, .4, .6, .8]
        self.blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
        # note: delta_sent is last delta_sent, new one will have to be calculated
        self.internal_variables = {'current_sent': self.blank_sent,
                                'last_sent': self.blank_sent,
                                'delta_sent': self.blank_sent,
                                'average_sent': self.blank_sent,
                                'average_delta': self.blank_sent,
                                'num_data': 0}
        self.c = Criterium(self.internal_variables, self.thresholds)

    def test_very_high(self):
        '''edgecases should round up'''
        pos = self.thresholds[0]
        calculation = self.c.reverse_calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'very high')

    def test_high(self):
        pos = self.thresholds[1]
        calculation = self.c.reverse_calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'high')

    def test_medium(self):
        pos = self.thresholds[2]
        calculation = self.c.reverse_calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'medium')

    def test_low(self):
        pos = self.thresholds[3]
        calculation = self.c.reverse_calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'low')

    def test_very_low(self):
        pos = self.thresholds[3] + .01
        calculation = self.c.reverse_calculate(pos, self.thresholds)
        self.assertTrue(calculation == 'very low')

    # def tearDown(self):
    #     self.thresholds.dispose()
    #     self.c.dispose()


class TestDownselect(unittest.TestCase):
    def setUp(self):
        self.thresholds = [.2, .4, .6, .8]
        self.blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
        self.blank_sent = {'neg': 0, 'pos':0, 'neu':0, 'compound': 0}
        # note: delta_sent is last delta_sent, new one will have to be calculated
        self.internal_variables = {'current_sent': self.blank_sent,
                                'last_sent': self.blank_sent,
                                'delta_sent': self.blank_sent,
                                'average_sent': self.blank_sent,
                                'average_delta': self.blank_sent,
                                'num_data': 0}
        self.c = Criterium(self.internal_variables, self.thresholds)

    def test_no_common(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        list3 = self.c.downselect(list1, list2)
        self.assertTrue(list3 == [])

    def test_all_common(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = self.c.downselect(list1, list2)
        self.assertTrue(list3 == [1, 2, 3])

    def test_some_common(self):
        list1 = [1, 2, 3]
        list2 = [2, 3, 4]
        list3 = self.c.downselect(list1, list2)
        self.assertTrue(list3 == [2, 3])


class Criterium:
    def __init__(self, internal_variables, thresholds):
        self.internal_variables = internal_variables
        self.thresholds = thresholds

    def calculate(self, val, thresholds=[.2, .4, .6, .8]):
        '''calculates val as very low, low, medium, high, or very high'''
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

    def reverse_calculate(self, val, thresholds=[.2, .4, .6, .8]):
        '''calculates criteria value as high when val is low
        and as low when val is high, rounds down'''
        # threshold between high and very high
        v_high_thres = thresholds[0]

        # threshold between medium and high
        high_thres = thresholds[1]

        # threshold between low and medium
        med_thres = thresholds[2]

        # threshold between very low and low
        low_thres = thresholds[3]

        if val <= v_high_thres:
            return 'very high'
        else:
            if val <= high_thres:
                return 'high'
            else:
                if val <= med_thres:
                    return 'medium'
                else:
                    if val <= low_thres:
                        return 'low'
                    else:
                        return 'very low'

    def downselect(self, list1, list2):
        '''downselects list2 to only the elements contiained in list1'''
        downselect_list = []
        for item in list1:
            if item in list2:
                downselect_list.append(item)
        return downselect_list

if __name__ == "__main__":
    unittest.main()
