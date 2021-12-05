calcstrats = {
    'subtraction': lambda x, y: x - y,
    'addition': lambda x, y: x + y,
    'multiplication': lambda x, y: x * y,
    'division': lambda x, y: x / y
    }

def printStrats(lst):
    for c in calcstrats.keys():
        print(c)
        
def operateOnInput(task):
    """Operate on user-defined input"""
    values = input('Enter two integers separated by a comma and whitespace: ')
    str_list = list(values.split(', '))
    int_list = list(map(int, str_list))
    
    result = calcstrats[task](
        int_list[0], 
        int_list[1]
        )
    print(f'The result is {result}')
    
def main():
    
    print('Welcome to the Small Calculator! What do you want to do? Available operations are')
    printStrats(calcstrats)
    task = input()
    operateOnInput(task)
            
    while True:
        continuation = input('Keep calculating? Enter Y for yes, or N for no: ')
        if continuation == 'Y':
            print('Choose your operation. Available operations are')
            printStrats(calcstrats)
            task = input()
            operateOnInput(task)
        elif continuation == 'N':
            print('Goodbye!')
            break
          
if __name__ == '__main__':
    main()

