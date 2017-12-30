# Collatz Sequence

def collatz(value):
    if value % 2 == 0:
        value = value // 2
        print(value)
        return value
    elif value % 2 == 1:
        value = 3 * value + 1
        print(value)
        return value    

def game():
    try:
        value = int(input("Enter a number: "))
        while value != 1:
            value = collatz(value)
    except ValueError:
        print("You must enter an integer")
        game()

game()
        
    




    
