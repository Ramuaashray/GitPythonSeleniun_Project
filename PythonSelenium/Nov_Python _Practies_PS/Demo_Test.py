class BasicCalculator:
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b

    def addition(self):
        return self.firstNumber + self.secondNumber

    def subtraction(self):
        return self.firstNumber - self.secondNumber

    def multiplication(self):
        return self.firstNumber * self.secondNumber

    def division(self):
        if self.secondNumber != 0:
            return self.firstNumber / self.secondNumber
        else:
            return "Division by zero is not allowed."