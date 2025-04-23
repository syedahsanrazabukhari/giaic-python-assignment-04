import random

num_of_rounds = 5
def main():
    print("Welcome to the High-Low Game!\n")
    print("---------------------------------------\n")
    score = 0
    
    for round in range(1, num_of_rounds +1):
      print(f"Round {round} of {num_of_rounds}")
      user_num = random.randint(1, 100)
      computer_num = random.randint(1, 100)
      print(f"User's number is ", user_num) 
      
      guess = ""
      while guess not in ["higher", "lower"]:
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").lower().strip()
        if guess not in ["higher", "lower"]:
             print("Invalid input. Please enter 'higher' or 'lower'. ")
      if guess == "higher" and user_num > computer_num or \
         guess == "lower" and user_num < computer_num:
          print("You guessed correctly! You win this round.")   
          score += 1
      else:
          print("You guessed incorrectly. You lose this round.")
   

      print(f"Computers number is {computer_num}\n")
      print(f"Your score is {score} out of {num_of_rounds}")

    print("\nThanks for playing!")
    if score == num_of_rounds:
     print("🌟 Wow! You played perfectly!")
    elif score > num_of_rounds / 2:
        print("👍 Good game!")
    else:
        print("😢 Aww! Better luck next time!")

if __name__ == "__main__":        
    main()