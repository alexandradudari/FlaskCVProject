import unittest
from click.testing import CliRunner
from manage import cli


class ShowCommandTests(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_show_personal_data(self):
        result = self.runner.invoke(cli, ["show", "personal"])
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Name", result.output)
        self.assertIn("Alexandra Dudari", result.output)

    def test_show_nonexistent_data(self):
        result = self.runner.invoke(cli, ["show", "skills"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), "No data available for 'skills'.")
        self.assertNotIn("Name", result.output)

    def test_show_invalid_argument(self):
        result = self.runner.invoke(cli, ["show"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: Missing argument 'DATA'", result.output)

    def test_show_with_empty_data(self):
        result = self.runner.invoke(cli, ["show", "empty_data"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), "No data available for 'empty_data'.")
