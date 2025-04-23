def print_ones_digit(num:int):
    result = num % 10
    print(result)

def main():
    user_input = int(input("Enter a number: "))
    print_ones_digit(user_input)

if __name__ == "__main__": 
    main()    