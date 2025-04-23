def main():
     dividend: int = int(input("Please enter an integer to be divided: "))
     divisor: int = int(input("Please enter an integer to divide by: "))
     quotient: int = dividend // divisor
     remender: int = dividend % divisor
     print(f"The result of this division is {quotient} with a remainder of {remender}")

if __name__ == '__main__':
    main()
   