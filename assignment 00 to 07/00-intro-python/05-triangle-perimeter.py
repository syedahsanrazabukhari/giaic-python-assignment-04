
def main():
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        perimeter = side1 + side2 + side3
        print("The perimeter of the triangle is:", perimeter)
    else:
        print("The given sides do not form a valid triangle.")

if __name__ == "__main__":        
    main()