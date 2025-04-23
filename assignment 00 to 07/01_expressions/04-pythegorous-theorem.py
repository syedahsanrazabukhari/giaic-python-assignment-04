import math

def main():
    ab: float = float(input("Enter the length of side a and b :"))
    ac: float = float(input("Enter the length of side c :"))
    bc: float = math.sqrt(ab** 2 + ac** 2)
    print("The length of side bc (the hypotenuse) is:", bc)

if __name__ == "__main__":    
  main()