import unittest
from unittest.mock import patch
from core import calculation


class TestCalc(unittest.TestCase):

    def test_get_severity_scores(self):
        calc = calculation.Calc([])
        calc.variables.response = [{'severities': ['critical'],
                                    'num_of_vulnerabilities':1,
                                    'num_of_dependencies': 2},
                                   {'severities': ['low'],
                                    'num_of_vulnerabilities':1,
                                    'num_of_dependencies': 2}]
        expected_severity_score = [[1], [0.1]]
        calc.get_severity_scores()
        calculated_severity_scores = calc.severity_scores
        self.assertEqual(calculated_severity_scores, expected_severity_score)

    def test_get_health_status(self):
        calc = calculation.Calc([])
        mock_o = {'severities': ['critical'],
                  'num_of_vulnerabilities': 1,
                  'num_of_dependencies': 2}
        mock_s = [1]
        expected_health_status_2 = 2
        calculated_health_status = calc.get_health_status(mock_o, mock_s)
        self.assertEqual(calculated_health_status, expected_health_status_2)

        calc = calculation.Calc([])
        mock_o = {'severities': ['critical'],
                  'num_of_vulnerabilities': 1,
                  'num_of_dependencies': 0}
        mock_s = [1]

        expected_health_status_0 = 0
        calculated_health_status = calc.get_health_status(mock_o, mock_s)
        self.assertEqual(calculated_health_status, expected_health_status_0)

    @patch.object(calculation.Calc, 'get_health_status')
    @patch.object(calculation.Calc, 'get_severity_scores')
    @patch.object(calculation.Calc, 'get_variables_all_objs')
    def test_all_statuses(self, mock_v, mock_s, mock_h):
        mock_h.return_value = 'dummy score'

        # More than 1
        calc = calculation.Calc([])
        calc.variables.response = [{'severities': ['critical'],
                                    'num_of_vulnerabilities':1,
                                    'num_of_dependencies': 2},
                                   {'severities': ['low', 'critical'],
                                    'num_of_vulnerabilities':2,
                                    'num_of_dependencies': 2}]

        calc.variables.repo_info = [None, None]
        calc.severity_scores = [[1], [0.1, 1]]
        expected_statuses = [('dummy score', None), ('dummy score', None)]
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, expected_statuses)

        # 1
        calc = calculation.Calc([])
        calc.variables.response = [{'severities': ['critical'],
                                    'num_of_vulnerabilities':1,
                                    'num_of_dependencies': 2}]

        calc.variables.repo_info = [None]
        calc.severity_scores = [[1]]
        expected_statuses = [('dummy score', None)]
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, expected_statuses)

        # 0
        calc = calculation.Calc([])
        calc.variables.response = []
        calc.variables.repo_info = []

        calc.severity_scores = ['N/A']
        expected_statuses = []
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, expected_statuses)

        # None object (bad message request)
        calc = calculation.Calc([])
        calc.variables.response = [None]
        calc.variables.repo_info = [None]
        calc.severity_scores = ['N/A']
        expected_statuses = ['N/A']
        calculated_all_statuses = calc.all_statuses()
        self.assertEqual(calculated_all_statuses, expected_statuses)


if __name__ == '__main__':

    unittest.main()
