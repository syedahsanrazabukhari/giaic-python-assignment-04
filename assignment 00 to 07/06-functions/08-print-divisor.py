def print_advisor(num):
    print(f"The divisors of {num} are: ", end="")
    for i in range(1, num +1):
        if num % i == 0:
            print(i, end=" ")

def main():
    user_input: int = int(input("Enter a number: "))
    print_advisor(user_input)

if __name__ == '__main__':    
    main()