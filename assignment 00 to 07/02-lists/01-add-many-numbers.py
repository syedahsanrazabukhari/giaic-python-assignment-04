def add_nums(numbers):
    total = 0
    for n in numbers:
        total += n
    return total
def main():
    numbers = [1, 2, 3, 4, 5]
    result = add_nums(numbers)
    print(f"The sum of the numbers is: {result}")

if __name__ == "__main__":
    main()