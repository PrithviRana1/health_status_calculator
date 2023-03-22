import unittest
from unittest.mock import patch
from core import calculation


class TestCalc(unittest.TestCase):

    @patch.object(calculation.Calc, 'variables')
    def test_get_severity_score(self, mock_v):
        mock_v.response = [{'severities': ['critical'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2},
                           {'severities': ['low'],
                           'num_of_vulnerabilities':1,
                            'num_of_dependencies': 2}]
        calc = calculation.Calc()
        test_severity_score = [[1], [0.1]]
        calc.get_severity_score()
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


if __name__ == '__main__':

    unittest.main()
