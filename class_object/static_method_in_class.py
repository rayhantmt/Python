class calculator():
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def div(a,b):
        return a/b
print(calculator.add(2,3))
print(calculator.sub(2,3))
print(calculator.mul(2,3))
print(calculator.div(2,3))