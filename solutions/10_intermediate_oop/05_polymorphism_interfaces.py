"""Reference solution for Mini-Program 5: Polymorphism and Interfaces."""

from math import pi, sqrt


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

    def describe(self):
        return "Unknown shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius**2

    def perimeter(self):
        return 2 * pi * self.radius

    def describe(self):
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"Rectangle {self.width} by {self.height}"


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        semiperimeter = self.perimeter() / 2
        return sqrt(
            semiperimeter
            * (semiperimeter - self.side_a)
            * (semiperimeter - self.side_b)
            * (semiperimeter - self.side_c)
        )

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def describe(self):
        return f"Triangle with sides {self.side_a}, {self.side_b}, and {self.side_c}"


def calculate_total_area(shapes):
    return sum(shape.area() for shape in shapes)


class Payment:
    def process_payment(self, amount):
        raise NotImplementedError

    def refund(self, amount):
        raise NotImplementedError

    def get_details(self):
        return "Unknown payment method"


class CreditCard(Payment):
    def __init__(self, cardholder, last_four):
        self.cardholder = cardholder
        self.last_four = last_four

    def process_payment(self, amount):
        return f"Charged ${amount:.2f} to card ending in {self.last_four}"

    def refund(self, amount):
        return f"Refunded ${amount:.2f} to card ending in {self.last_four}"

    def get_details(self):
        return f"Credit card ending in {self.last_four}"


class PayPal(Payment):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Charged ${amount:.2f} through PayPal"

    def refund(self, amount):
        return f"Refunded ${amount:.2f} through PayPal"

    def get_details(self):
        return f"PayPal account {self.email}"


class Bitcoin(Payment):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def process_payment(self, amount):
        return f"Recorded ${amount:.2f} Bitcoin payment"

    def refund(self, amount):
        return f"Recorded ${amount:.2f} Bitcoin refund"

    def get_details(self):
        return f"Bitcoin wallet {self.wallet_address}"


class PaymentProcessor:
    def process_transaction(self, payment_method, amount):
        return payment_method.process_payment(amount)


class Animal:
    sound = "Some sound"
    movement = "Move"

    def make_sound(self):
        return self.sound

    def move(self):
        return self.movement

    def eat(self):
        return f"{type(self).__name__} is eating"


class Dog(Animal):
    sound, movement = "Bark", "Run"


class Cat(Animal):
    sound, movement = "Meow", "Walk"


class Bird(Animal):
    sound, movement = "Chirp", "Fly"


class Fish(Animal):
    sound, movement = "Bubble", "Swim"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def feed_all_animals(self):
        return [animal.eat() for animal in self.animals]

    def make_all_sounds(self):
        return [animal.make_sound() for animal in self.animals]


class Database:
    label = "database"

    def __init__(self):
        self.connected = False
        self.records = []

    def connect(self):
        self.connected = True
        return f"Connected to {self.label}"

    def disconnect(self):
        self.connected = False
        return f"Disconnected from {self.label}"

    def query(self, sql):
        return list(self.records)

    def insert(self, data):
        self.records.append(data)
        return f"Inserted into {self.label}"


class MySQLDatabase(Database):
    label = "MySQL"


class PostgreSQLDatabase(Database):
    label = "PostgreSQL"


class SQLiteDatabase(Database):
    label = "SQLite"


class DataManager:
    def migrate_data(self, source_db, target_db):
        records = source_db.query("SELECT * FROM records")
        for record in records:
            target_db.insert(record)
        return len(records)


class EmailNotifier:
    def send(self, message):
        return f"Email sent: {message}"


class SMSNotifier:
    def send(self, message):
        return f"SMS sent: {message}"


class PushNotifier:
    def send(self, message):
        return f"Push notification sent: {message}"


def notify_all(notifiers, message):
    return [notifier.send(message) for notifier in notifiers]


class Vehicle:
    label = "Vehicle"

    def start(self):
        return f"{self.label} started"

    def stop(self):
        return f"{self.label} stopped"

    def accelerate(self, speed):
        return f"{self.label} accelerated to {speed}"

    def brake(self):
        return f"{self.label} braked"


class Car(Vehicle):
    label = "Car"


class Motorcycle(Vehicle):
    label = "Motorcycle"


class Truck(Vehicle):
    label = "Truck"


class Bicycle(Vehicle):
    label = "Bicycle"

    def start(self):
        return "Bicycle: starting to pedal"


class TrafficSimulator:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def start_all(self):
        return [vehicle.start() for vehicle in self.vehicles]

    def simulate_traffic(self):
        return [
            (vehicle.accelerate(20), vehicle.brake(), vehicle.stop())
            for vehicle in self.vehicles
        ]


class Plugin:
    def load(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError

    def unload(self):
        raise NotImplementedError


class GreetingPlugin(Plugin):
    def load(self):
        return "Greeting plugin loaded"

    def execute(self):
        return "Hello from the greeting plugin"

    def unload(self):
        return "Greeting plugin unloaded"


class CountPlugin(Plugin):
    def __init__(self, items):
        self.items = items

    def load(self):
        return "Count plugin loaded"

    def execute(self):
        return len(self.items)

    def unload(self):
        return "Count plugin unloaded"


class PluginManager:
    def __init__(self):
        self.plugins = []

    def load_plugin(self, plugin):
        self.plugins.append(plugin)
        return plugin.load()

    def execute_plugins(self):
        return [plugin.execute() for plugin in self.plugins]

    def unload_plugins(self):
        results = [plugin.unload() for plugin in self.plugins]
        self.plugins.clear()
        return results


if __name__ == "__main__":
    shapes = [Circle(2), Rectangle(3, 4), Triangle(3, 4, 5)]
    print(calculate_total_area(shapes))
    print(PaymentProcessor().process_transaction(PayPal("student@example.com"), 12.50))
    zoo = Zoo()
    zoo.add_animal(Dog())
    zoo.add_animal(Bird())
    print(zoo.make_all_sounds())
    traffic = TrafficSimulator()
    traffic.add_vehicle(Car())
    traffic.add_vehicle(Bicycle())
    print(traffic.start_all())
