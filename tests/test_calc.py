import unittest
from unittest.mock import patch
from core import calculation


class TestCalc(unittest.TestCase):

    @patch.object(calculation.Calc, 'variables')
    def test_get_severity_scores(self, mock_v):
        mock_v.response = [{'severities': ['critical'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2},
                           {'severities': ['low'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2}]
        calc = calculation.Calc()
        test_severity_score = [[1], [0.1]]
        calc.get_severity_scores()
        calculated_severity_scores = calc.severity_scores
        self.assertEqual(calculated_severity_scores, test_severity_score)

    def test_get_health_status(self):
        mock_o = {'severities': ['critical'],
                  'num_of_vulnerabilities': 1,
                  'num_of_dependencies': 2}
        mock_s = [1]
        calc = calculation.Calc()
        test_health_status_2 = 2
        calculated_health_status = calc.get_health_status(mock_o, mock_s)
        self.assertEqual(calculated_health_status, test_health_status_2)

        mock_o = {'severities': ['critical'],
                  'num_of_vulnerabilities': 1,
                  'num_of_dependencies': 0}
        mock_s = [1]
        calc = calculation.Calc()
        test_health_status_0 = 0
        calculated_health_status = calc.get_health_status(mock_o, mock_s)
        self.assertEqual(calculated_health_status, test_health_status_0)

    @patch.object(calculation.Calc, 'get_health_status')
    @patch.object(calculation.Calc, 'get_severity_scores')
    @patch.object(calculation.Calc, 'variables')
    def test_all_statuses(self, mock_v, mock_s, mock_h):
        mock_h.return_value = 'dummy score'

        # More than 1

        mock_v.response = [{'severities': ['critical'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2},
                           {'severities': ['low', 'critical'],
                           'num_of_vulnerabilities':2,
                            'num_of_dependencies': 2}]
        calc = calculation.Calc()
        calc.severity_scores = [[1], [0.1, 1]]
        test_statuses = ['dummy score', 'dummy score']
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, test_statuses)

        # 1
        mock_v.response = [{'severities': ['critical'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2}
                           ]
        calc = calculation.Calc()
        calc.severity_scores = [[1]]
        test_statuses = ['dummy score']
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, test_statuses)

        # 0
        mock_v.response = []
        calc = calculation.Calc()
        calc.severity_scores = ['N/A']
        test_statuses = []
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, test_statuses)

        # None object (bad message request)
        mock_v.response = [None]
        calc = calculation.Calc()
        calc.severity_scores = ['N/A']
        test_statuses = ['N/A']
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, test_statuses)


if __name__ == '__main__':

    unittest.main()
