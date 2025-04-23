import random

def chaotic_counting():
   for i in range(1,11):
     if done():
      return
     print(i)

def done():
  return random.random() < 0.4


def main():
  print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
  chaotic_counting()
  print("I'm done counting.")

if __name__ == "__main__":
   main()