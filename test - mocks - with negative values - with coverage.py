import unittest
from unittest.mock import patch
import coverage

# Start coverage measurement
cov = coverage.Coverage()
cov.start()

class Calculator:
    def add_integers(self, a, b):
        if a < 0 or b < 0:
            return None
        return a + b

    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return self.add_integers(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            raise TypeError("Both arguments must be numeric types")

class TestCalculator(unittest.TestCase):

    @patch.object(Calculator, 'add_integers')
    def test_add_integers_called(self, mock_add_integers):
        calculator = Calculator()
        mock_add_integers.return_value = 6
        result = calculator.add(2, 4)
        mock_add_integers.assert_called_once_with(2, 4)
        self.assertEqual(result, 6)

    def test_add_positive_integers(self):
        calculator = Calculator()
        result = calculator.add(12, 3)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()

# Stop coverage measurement and save the results
cov.stop()
cov.save()

# Report the coverage
coverage_percentage = round(cov.report() * 100, 2)
print(f"Code coverage: {coverage_percentage}%")

cov.html_report(directory='coverage_html_report')  # Optional: Generate an HTML report
