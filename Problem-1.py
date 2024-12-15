class Calculator:
    def __init__(self, a, b, operation_type):
        self.a = a
        self.b = b
        self.operation_type = operation_type
    
    def calculate(self):
        if self.operation_type == 1:
            return self.a + self.b, "addition"
        elif self.operation_type == 2:
            return self.a - self.b, "subtraction"
        elif self.operation_type == 3:
            return self.a * self.b, "multiplication"
        elif self.operation_type == 4:
            if self.b != 0:
                return self.a / self.b, "division"
            else:
                return "Error: Division by zero", "division"
        else:
            return "Error: Invalid operation", ""

a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
operation = int(input("Enter the operation (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "))

calculator = Calculator(a, b, operation)
result, operation_name = calculator.calculate()
print(f"The result of {operation_name} is: {result}")
