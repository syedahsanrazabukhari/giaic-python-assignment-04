


import random

NUM_SIDES = 6

def dice_roll():
    dei1 :int = random.randint(1, NUM_SIDES)
    dei2 :int = random.randint(1, NUM_SIDES)
    total: int= dei1 + dei2
    print("Total of two dice:", total)

def main():
    dei1= 10
    print("die1 in main() starts as:" + str(dei1))
    dice_roll()
    # dice_roll()
    # dice_roll()

    print("die1 in main() is now:" + str(dei1))

if __name__ == "__main__":
    main()