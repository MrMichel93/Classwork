"""Student self-checks for the basic OOP worksheets."""

from starter_tests._support import WorksheetTestCase


class BasicOOPSelfChecks(WorksheetTestCase):
    def test_simple_class(self):
        worksheet = self.load("09_basic_oop", "01_simple_class.py")
        dog = self.require_class(worksheet, "Dog")
        self.assertTrue(hasattr(dog(), "__dict__"))
        self.require_class(worksheet, "Person")("Avery", 16)
        self.require_class(worksheet, "Book")("Python", "Ada", 100)
        self.require_class(worksheet, "Rectangle")(4, 6)

    def test_class_attributes(self):
        worksheet = self.load("09_basic_oop", "02_class_attributes.py")
        car = self.require_class(worksheet, "Car")
        self.assertEqual(car("Toyota", "Camry").wheels, 4)
        account = self.require_class(worksheet, "BankAccount")
        self.assertEqual(account("Avery", 25).bank_name, "Python Bank")
        student = self.require_class(worksheet, "Student")
        before = student.total_students
        student("Avery", 11)
        self.assertEqual(student.total_students, before + 1)

    def test_class_methods(self):
        worksheet = self.load("09_basic_oop", "03_class_methods.py")
        calculator = self.require_class(worksheet, "Calculator")
        self.require_method(calculator, "add", worksheet)
        self.require_method(calculator, "subtract", worksheet)
        self.require_method(calculator, "get_result", worksheet)
        value = calculator()
        value.add(10)
        value.subtract(3)
        self.assertEqual(value.get_result(), 7)
        circle = self.require_class(worksheet, "Circle")
        self.assertAlmostEqual(circle(5).calculate_area(), 78.53975)
        counter = self.require_class(worksheet, "Counter")()
        counter.increment()
        self.assertEqual(counter.get_count(), 1)

    def test_multiple_objects(self):
        worksheet = self.load("09_basic_oop", "04_multiple_objects.py")
        product = self.require_class(worksheet, "Product")
        self.assertEqual(product("Book", 10, 3).get_total_value(), 30)
        student = self.require_class(worksheet, "Student")("Avery", 16, [80, 100])
        student.add_grade(90)
        self.assertEqual(student.calculate_average(), 90)
        library = self.require_class(worksheet, "Library")()
        book = self.require_class(worksheet, "Book")("Python", "Ada")
        library.add_book(book)
        self.assertTrue(library.checkout_book("Python"))

    def test_composition_aggregation(self):
        worksheet = self.load("09_basic_oop", "05_composition_aggregation.py")
        address = self.require_class(worksheet, "Address")("1 Main", "Town", "ST", "12345")
        self.assertIn("Town", address.get_full_address())
        student = self.require_class(worksheet, "Student")("Avery", "S1")
        course = self.require_class(worksheet, "Course")("CS1", "Python", 3)
        student.add_course(course)
        self.assertEqual(student.get_total_credits(), 3)
        engine = self.require_class(worksheet, "Engine")(100, "gas")
        car = self.require_class(worksheet, "Car")("Make", "Model", 2024, engine)
        car.start_car()
        self.assertTrue(engine.running)
