class Calculator:
    def sum(self, a,b):
        return a + b
    def sub(self, a,b):
        return a - b
    def mult(self, a,b):
        return a * b
    def div(self, a,b):
        if b == 0:
            return ValueError("Erro matemático: Divisão por 0")
        return a/b