class Estimates:
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def estimate_calculation(self):
        return (self.a + 4 * self.m + self.b) / 6

    def standard_deviation_calculation(self):
        return (self.b - self.a) / 6