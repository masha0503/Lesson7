class Calculation:
    typeOperation: str
    def __init__(self, typeOperation: str):
        self.typeOperation = typeOperation

    def __str__(self):
        return f'operation \"{self.typeOperation}\"'

    def __call__(self, a: float, b: float):
        if self.typeOperation == '/' and b != 0:
            return a / b
        elif self.typeOperation == '-':
            return a - b
        elif self.typeOperation == '*':
            return a * b
        elif self.typeOperation == '+':
            return a + b
        else:
            raise f'operation \"{self.typeOperation}\" has not realization'

sumNumbers = Calculation(typeOperation='/')
result = sumNumbers(a=5, b=2)
print(result)
print(sumNumbers)