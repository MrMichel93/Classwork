"""Tests for intermediate OOP reference solutions."""

import contextlib
import io
import unittest

from solution_loader import load_solution


class IntermediateOOPTests(unittest.TestCase):
    def test_inheritance(self):
        lesson = load_solution("10_intermediate_oop", "01_inheritance.py")
        dog = lesson.Dog("Buddy", "Canine")
        self.assertEqual((dog.name, dog.species), ("Buddy", "Canine"))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            lesson.Car("Toyota", "Camry", 2024).honk()
            lesson.Motorcycle("Honda", "CBR", 2023).rev_engine()
        self.assertEqual(output.getvalue().splitlines(), ["Beep beep!", "Vroom vroom!"])
        self.assertEqual(lesson.TeslaCar("Tesla", "3", 2024, 75).autopilot(), "Autopilot enabled")

    def test_method_overriding(self):
        lesson = load_solution("10_intermediate_oop", "02_method_overriding.py")
        self.assertEqual(lesson.Rectangle("screen", 4, 6).area(), 24)
        self.assertAlmostEqual(lesson.Circle("coin", 5).area(), 78.53975)
        self.assertEqual(
            [animal.speak() for animal in (lesson.Dog("D"), lesson.Cat("C"), lesson.Cow("W"))],
            ["Woof!", "Meow!", "Moo!"],
        )
        self.assertEqual(lesson.Manager("Avery", 50000).calculate_bonus(), 10000)
        self.assertEqual(str(lesson.Person("Avery", 16)), "Avery is 16 years old")

    def test_super_function(self):
        lesson = load_solution("10_intermediate_oop", "03_super_function.py")
        student = lesson.Student("Avery", 16, "S1")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            student.introduce()
        self.assertEqual(
            output.getvalue().splitlines(),
            ["Hi, I'm Avery, 16 years old", "My student ID is S1"],
        )
        account = lesson.SavingsAccount("1", 100)
        with contextlib.redirect_stdout(io.StringIO()):
            account.deposit(50)
        self.assertAlmostEqual(account.balance, 151.5)

    def test_polymorphism_interfaces(self):
        lesson = load_solution("10_intermediate_oop", "05_polymorphism_interfaces.py")
        shapes = [lesson.Circle(1), lesson.Rectangle(3, 4), lesson.Triangle(3, 4, 5)]
        self.assertAlmostEqual(lesson.calculate_total_area(shapes), 18 + 3.141592653589793)
        self.assertEqual(
            lesson.PaymentProcessor().process_transaction(lesson.PayPal("a@example.com"), 5),
            "Charged $5.00 through PayPal",
        )
        zoo = lesson.Zoo()
        zoo.add_animal(lesson.Dog())
        zoo.add_animal(lesson.Fish())
        self.assertEqual(zoo.make_all_sounds(), ["Bark", "Bubble"])
        source, target = lesson.SQLiteDatabase(), lesson.MySQLDatabase()
        source.insert({"id": 1})
        self.assertEqual(lesson.DataManager().migrate_data(source, target), 1)
        self.assertEqual(target.records, [{"id": 1}])
        traffic = lesson.TrafficSimulator()
        traffic.add_vehicle(lesson.Bicycle())
        self.assertEqual(traffic.start_all(), ["Bicycle: starting to pedal"])
        plugins = lesson.PluginManager()
        self.assertEqual(plugins.load_plugin(lesson.GreetingPlugin()), "Greeting plugin loaded")
        self.assertEqual(plugins.execute_plugins(), ["Hello from the greeting plugin"])
