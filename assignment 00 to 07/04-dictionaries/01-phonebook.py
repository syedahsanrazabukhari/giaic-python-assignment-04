def read_phone_numbers():
    phone_books = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        phone_numbers = input("Phone numbers (comma-separated): ").split(",")
        phone_books[name] = phone_numbers

    return phone_books

def print_phone_books(phone_books):
    for name in phone_books:
        print(str(name),"->"+str(phone_books))


def lockup_phone_books(phone_books):
    while True:
        name= input ("Enter name : ")
        if name == "":
            break
        if name not in phone_books:
            print("Name not found in " + str(phone_books))

        else:
            print(phone_books[name])
def main():
    phone_books = read_phone_numbers()
    print_phone_books(phone_books)
    lockup_phone_books(phone_books)


if __name__ == "__main__":
    main()                

            