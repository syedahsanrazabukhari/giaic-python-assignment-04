"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
import random

NUM_SIDES: int = 6

def main():
    die1 :int = random.randint(1, NUM_SIDES)
    die2 :int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print ("Dice have", NUM_SIDES, "sides each.")
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == "__main__":
    main()    