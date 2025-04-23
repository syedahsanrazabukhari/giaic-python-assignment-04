adult_age : int = 18
def is_adult(age: int) :
    if age >= adult_age:
        return True
    return False
def main ():
    user_age = int(input("Enter your age: "))
    if is_adult(user_age):
        print("You are an adult")
    else:
        print("You are not an adult")

if __name__ == '__main__':
 main()