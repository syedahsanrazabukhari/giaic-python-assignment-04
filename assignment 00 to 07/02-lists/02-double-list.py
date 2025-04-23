def main():
    numbers = [2,4,6,8,10]
    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2
        print(f"Element at index {i}: {elem_at_index} * 2 = {numbers[i]}")


if __name__ == "__main__":
    main()