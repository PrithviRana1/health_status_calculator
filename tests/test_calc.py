import unittest
from unittest.mock import patch
from core import calculation


class TestCalc(unittest.TestCase):

    @patch.object(calculation.calc, 'variables')
    def test_get_severity_score(self, mock_v):
        mock_v.severities = ['critical']
        calc = calculation.calc()
        test_severity_score = [1]
        calc.get_severity_score()
        calculated_severity_score = calc.severity_score
        self.assertEqual(calculated_severity_score, test_severity_score)

    @patch.object(calculation.calc, 'get_severity_score')
    @patch.object(calculation.calc, 'variables')
    def test_get_health_status(self, mock_v, mock_s):
        mock_v.num_of_dependencies = 1
        calc = calculation.calc()
        calc.severity_score = [1]
        mock_v.num_of_vulnerabilities = 1
        health_status_1 = calc.get_health_status()
        mock_v.num_of_vulnerabilities = 0
        health_status_0 = calc.get_health_status()

        # Non-zero vulnerabilities
        self.assertEqual(health_status_1, 1)

        # Zero vulnerabilities
        self.assertEqual(health_status_0, 0)


if __name__ == '__main__':

    unittest.main()
