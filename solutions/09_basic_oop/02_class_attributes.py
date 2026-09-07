"""Reference solution for Mini-Program 2: Class Attributes."""


class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model


class BankAccount:
    bank_name = "Python Bank"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


class Student:
    school = "Python High School"
    total_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1


class InstanceTracker:
    total_instances = 0

    def __init__(self):
        InstanceTracker.total_instances += 1


if __name__ == "__main__":
    car1, car2 = Car("Toyota", "Camry"), Car("Honda", "Civic")
    account1, account2 = BankAccount("Avery", 100), BankAccount("Jordan", 250)
    students = [Student("Avery", 11), Student("Jordan", 12), Student("Casey", 11)]
    BankAccount.bank_name = "New Python Bank"
    print(car1.wheels, car2.wheels, Car.wheels)
    print(car1.make, car2.model)
    print(account1.bank_name, account2.bank_name)
    print(Student.total_students, students[0].school)
