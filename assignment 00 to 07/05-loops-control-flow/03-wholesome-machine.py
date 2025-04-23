affir : str = "I am capable of doing anything I put my mind to."

def main():
   print("Please type the following affirmation: " + affir)
   user_input = input("type here: ")

   while user_input != affir:
      print("That was not the affirmation. ")
      print("Please type the following affirmation: " + affir)
      user_input = input("type here: ")

   print("That's right! :)")  

if __name__ == '__main__':
    main()