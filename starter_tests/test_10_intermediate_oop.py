"""Student self-checks for the intermediate OOP worksheets."""

from starter_tests._support import WorksheetTestCase


class IntermediateOOPSelfChecks(WorksheetTestCase):
    def test_inheritance(self):
        worksheet = self.load("10_intermediate_oop", "01_inheritance.py")
        animal = self.require_class(worksheet, "Animal")
        dog = self.require_class(worksheet, "Dog")
        self.assertIsInstance(dog("Buddy", "Canine"), animal)
        self.require_method(self.require_class(worksheet, "Car"), "honk", worksheet)
        self.require_method(self.require_class(worksheet, "Motorcycle"), "rev_engine", worksheet)

    def test_method_overriding(self):
        worksheet = self.load("10_intermediate_oop", "02_method_overriding.py")
        rectangle = self.require_class(worksheet, "Rectangle")
        self.assertEqual(rectangle("screen", 4, 6).area(), 24)
        self.assertEqual(self.require_class(worksheet, "Dog")("Buddy").speak(), "Woof!")
        self.assertEqual(self.require_class(worksheet, "Manager")("Avery", 50000).calculate_bonus(), 10000)

    def test_super_function(self):
        worksheet = self.load("10_intermediate_oop", "03_super_function.py")
        person = self.require_class(worksheet, "Person")
        student = self.require_class(worksheet, "Student")
        self.assertIsInstance(student("Avery", 16, "S1"), person)
        electric_car = self.require_class(worksheet, "ElectricCar")("Tesla", "3", 75)
        self.assertEqual(electric_car.battery_capacity, 75)
        account = self.require_class(worksheet, "SavingsAccount")("1", 100)
        account.deposit(50)
        self.assertAlmostEqual(account.balance, 151.5)

    def test_polymorphism_interfaces(self):
        worksheet = self.load("10_intermediate_oop", "05_polymorphism_interfaces.py")
        total_area = self.require_callable(worksheet, "calculate_total_area")
        circle = self.require_class(worksheet, "Circle")
        rectangle = self.require_class(worksheet, "Rectangle")
        self.assertAlmostEqual(total_area([circle(1), rectangle(3, 4)]), 12 + 3.141592653589793)
        payment = self.require_class(worksheet, "PayPal")("student@example.com")
        processor = self.require_class(worksheet, "PaymentProcessor")()
        self.assertIn("PayPal", processor.process_transaction(payment, 5))
        bicycle = self.require_class(worksheet, "Bicycle")()
        self.assertTrue(callable(getattr(bicycle, "start", None)), "Bicycle must implement start().")
        self.assertIn("pedal", bicycle.start().lower())
