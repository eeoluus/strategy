from abc import ABC, abstractmethod

class CalcStrat(ABC):
    """Interface for calculation strategies"""
    @abstractmethod
    def operation(self, x, y):
        pass
    
class Subtraction(CalcStrat):
    def operation(self, x, y):
        return x - y
    
class Addition(CalcStrat):
    def operation(self, x, y):
        return x + y

class Multiplication(CalcStrat):
    def operation(self, x, y):
        return x * y
    
class Division(CalcStrat):
    def operation(self, x, y):
        return x / y    
    
class Calculator():
    """Initialize to specify two operands and the operation"""
    def __init__(self, x, y, calcstrat: CalcStrat):
        self.x = x
        self.y = y
        self.calcstrat = calcstrat
        
    def calculate(self):
        return self.calcstrat.operation(
            self, 
            self.x, 
            self.y
            )

def operateOnInput(task):
    """Operate on user-defined input"""
    values = input('Enter two integers separated by a comma and whitespace: ')
    str_list  = list(values.split(', '))
    int_list = list(map(int, str_list))

    for Operation in CalcStrat.__subclasses__():
        if Operation.__name__ == task:
            test = Calculator(
                int_list[0], 
                int_list[1], 
                Operation
                )
            print(f'The result is {test.calculate()}')    

def main():
    
    print('Welcome to the Small Calculator! What do you want to do? Available operations are')
    for Operation in CalcStrat.__subclasses__():
        print(Operation.__name__) 
    task = input()
    operateOnInput(task)
            
    while True:
        continuation = input('Keep calculating? Enter Y for yes, or N for no: ')
        if continuation == 'Y':
            print('Choose your operation. Available operations are')
            for Operation in CalcStrat.__subclasses__():
                print(Operation.__name__)
            task = input()
            operateOnInput(task)
        elif continuation == 'N':
            print('Goodbye!')
            break
          
if __name__ == '__main__':
    main()

