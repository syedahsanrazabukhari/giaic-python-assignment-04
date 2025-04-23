def range_in(n,low,high):
    if n >= low and n <= high:
        return True
    return False
def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))

    print(range_in(n,low,high))
if __name__ == '__main__':
    main()