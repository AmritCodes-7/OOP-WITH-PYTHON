# creating a calculator using class


class Calculator:
    def addition(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
        self.sum = self.number1 + self.number2
        return self.sum


calc = Calculator()
calc.num1 = 34
calc.num2 = 1
add = calc.addition(calc.num1, calc.num2)

print(f"{add}")
