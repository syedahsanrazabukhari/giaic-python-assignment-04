def get_user_data():
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last: ")
    your_email = input("Enter Your Email: ")

    return first_name, last_name, your_email
def main():
    user_data = get_user_data()
    print(f"Your name is {user_data[0]} {user_data[1]} and your email is {user_data[2]}")

if __name__ == "__main__":   
    main()