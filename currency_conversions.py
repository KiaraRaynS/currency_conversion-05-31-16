

class Money:

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def convert_to_currency(self, other):
        if self.currency == 'JPY':
            if other.currency == 'USD':
                return self.converted_value * .00903
            elif other.currency == 'EUR':
                return self.converted_value * .00811
            elif other.currency == 'BTC':
                return self.converted_value * .000017

    def get_value(self):
        if self.currency == 'USD':
            return self.value*1
            # EUR = self.value * .898
            # JPY = self.value * 110.713
            # BTC = self.value * .0019
        elif self.currency == 'JPY':
            return self.value * .00903
            # USD = self.value * .00903
            # EUR = self.value * .00811
            # BTC = self.value * .000017
        elif self.currency == 'BTC':
            return self.value * 529.39
            # USD = self.value * 529.39
            # EUR = self.value * 477.13
            # JPY = self.value * 58806.10
        elif self.currency == 'EUR':
            return self.value * 1.113
            # USD = self.value * 1.113
            # JPY = self.value * 123.264
            # BTC = self.value * .0021

    def __eq__(self, other):
        return self.get_value() == other.get_value()

    def __ne__(self, other):
        return self.get_value() != other.get_value()

    def __le__(self, other):
        return self.get_value() <= other.get_value()

    def __lt__(self, other):
        return self.get_value() < other.get_value()

    def __ge__(self, other):
        return self.get_value() >= other.get_value()

    def __gt__(self, other):
        return self.get_value() > other.get_value()

    def __add__(self, other):
        return self.get_value() + self.get_value()

    def __sub__(self, other):
        return self.get_value() - other.get_value()

    def __mul__(self, other):
        return self.get_value() * other.get_value()

    def __mod__(self, other):
        return self.get_value() % other.get_value()

test_1 = Money(1, 'BTC')
test_2 = Money(6, 'EUR')
print(test_1 == test_2)
print(test_2 + test_1)
print(test_2 % test_1)
