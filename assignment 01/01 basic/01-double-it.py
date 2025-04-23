def main():
    user_input_num = int(input("Enter a number: "))
    while user_input_num < 100:
        user_input_num *= 2
        print(user_input_num)

if __name__ == "__main__":
   main()