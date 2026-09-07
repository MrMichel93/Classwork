"""Reference solution for Mini-Program 3: Using super()."""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"My student ID is {self.student_id}")


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Vehicle starting")


class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def start(self):
        super().start()
        print("Electric motor engaged")


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        super().deposit(amount)
        self.balance *= 1.01
        print("Interest applied")


class Mammal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an animal"


class WarmBloodedMammal(Mammal):
    def describe(self):
        return f"{super().describe()} and warm-blooded"


class FamilyDog(WarmBloodedMammal):
    def describe(self):
        return f"{super().describe()} and a dog"


if __name__ == "__main__":
    student = Student("Avery", 16, "S100")
    student.introduce()
    electric_car = ElectricCar("Tesla", "Model 3", 75)
    electric_car.start()
    savings = SavingsAccount("1001", 100)
    savings.deposit(50)
    print(savings.balance)
