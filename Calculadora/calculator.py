class Calculator:
    def sum(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mult(a,b):
        return a * b
    def div(a,b):
        if b == 0:
            raise ZeroDivisionError('Erro matemático: Divisão por 0')
        return a/b