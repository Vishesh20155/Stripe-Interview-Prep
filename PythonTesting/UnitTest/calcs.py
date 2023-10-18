class Calculations:
    def __init__(self, a: int, b: int):
        print("@@@", type(a), type(b))
        if type(a) not in ['int', 'float'] or type(b) not in ['int', 'float']:
            raise TypeError('Inputs must be int or float')
        self.a = a
        self.b = b

    def get_sum(self):
        return self.a + self.b

    def get_difference(self):
        return self.a - self.b

    def get_product(self):
        return self.a * self.b

    def get_quotient(self):
        return self.a / self.b