def double_num(num: int):
    return num * 2

def main():
    user_input = int(input("Enter a number: "))
    result = double_num(user_input)
    print(f"The double of {user_input} is {result}")

if __name__ == "__main__":
    main()