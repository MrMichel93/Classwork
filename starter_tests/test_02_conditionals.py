"""Student self-checks for topic 02 worksheets."""

from starter_tests._support import WorksheetTestCase


class ConditionalSelfChecks(WorksheetTestCase):
    def test_grade_checker_output(self):
        worksheet = self.load("02_conditionals", "01_grade_checker.py")
        self.assert_output_contains(
            worksheet, "Grade: B",
            instruction="use the default score of 85 and print its B grade.",
        )

    def test_age_classifier_has_branches(self):
        worksheet = self.load("02_conditionals", "02_age_classifier.py")
        self.assert_conditional_structure(
            worksheet,
            "use if/elif/else to classify age and separate if statements for allowed activities.",
        )

    def test_number_comparator_output(self):
        worksheet = self.load("02_conditionals", "03_number_comparator.py")
        self.assert_output_contains(
            worksheet, "second number is larger", "5", "num1 and num3 are equal",
            instruction="compare 15, 20, and 15 and print the stated relationship and difference.",
        )

    def test_password_validator_output(self):
        worksheet = self.load("02_conditionals", "04_password_validator.py")
        self.assert_output_contains(
            worksheet, "Length is good", "Contains a number", "Passwords match", "Password is valid",
            instruction="validate the supplied Secret123 password and print each relevant result.",
        )
