from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    while True:
        print('Select a function to use:')
        print('Factorial - 1')
        print('Square a number - 2')
        print('Cube a number - 3')
        print('Square root - 4')
        print('Cube root - 5')
        print('Logarithm - 6')
        print('Natural logarithm - 7')
        print('Common logarithm - 8')
        print('Exit - 9')
        choice = int(input('Enter your choice: ').strip())
        if choice == 9:
            print('Exit')
            break
        try:
            if choice == 1:
                x = int(input('Enter a non-negative integer: '))
                print(f'Factorial of {x} is {fact(x)}')
            elif choice == 2:
                i = float(input('Enter a number: '))
                print(f'{i} squared is {exp2(i)}')
            elif choice == 3:
                i = float(input('Enter a number: '))
                print(f'{i} cubed is {exp3(i)}')
            elif choice == 4:
                i = float(input('Enter a non-negative number: '))
                print(f'Square root of {i} is {root2(i)}')
            elif choice == 5:
                i = float(input('Enter a number: '))
                print(f'Cube root of {i} is {root3(i)}')
            elif choice == 6:
                a = float(input('Enter the base (a > 0, a != 1): '))
                b = float(input('Enter the number (b > 0): '))
                print(f'log_{a}({b}) is {log(a, b)}')
            elif choice == 7:
                b = float(input('Enter the number (b > 0): '))
                print(f'ln({b}) is {ln(b)}')
            elif choice == 8:
                b = float(input('Enter the number (b > 0): '))
                print(f'lg({b}) is {lg(b)}')
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()