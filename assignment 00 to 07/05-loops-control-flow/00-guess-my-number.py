import random

def main():
    secret_num = random.randint(1,99)
    print("I am thinking a number between 1 to 99..... ")
    guess_user_input = int(input("Enter a guess number... "))

    while guess_user_input != secret_num:
       if guess_user_input < secret_num:
           print(f"{guess_user_input}Your guess is too low")
       else: 
        print(guess_user_input , "Your guess is too high")

       print()  
       guess_user_input = int(input("Enter a new guess number... "))
     
       
    print("Congrats! The number was: " + str(secret_num))

if __name__ == '__main__' :
   main()       