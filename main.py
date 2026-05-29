
# 80. Property Validation
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value

p = Product(500)
print(p.price)


# 81. Bank Transfer
class Bank:
    def __init__(self, money):
        self.money = money

    def transfer(self, other, amount):
        self.money -= amount
        other.money += amount

a = Bank(1000)
b = Bank(500)

a.transfer(b, 200)
print(a.money, b.money)


# 82. Employee Bonus
class Employee:
    def __init__(self, salary):
        self.salary = salary

    def total(self):
        return self.salary + self.salary * 0.1

print(Employee(1000).total())

