import random

def main():
    secret_num= random.randint(1,100)
    print("I am thinking a number between 1 to 100..... ")
    user_input=int(input("Enter a Number: "))

    while user_input != secret_num:
       if user_input < secret_num:
            print("Your guess is too low")
       else :
            print("Your guess is too high")    
       print("I am thinking a number between 1 to 100..... ")
       user_input=int(input("Enter a Number: "))   
    print("Congrats! The number was: " + str(secret_num))

if __name__ == "__main__":        
    main()