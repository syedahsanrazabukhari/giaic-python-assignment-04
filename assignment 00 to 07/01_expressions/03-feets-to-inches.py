INCHES_IN_FOOT: int = 12  

def main():
        # Prompt user for length in inches
        feet = float(input("Enter the number of feet : "))
        inches :float = feet * INCHES_IN_FOOT
        print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":    
    main()