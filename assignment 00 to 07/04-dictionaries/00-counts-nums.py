def get_user_num():
    user_num = []
    while True:
        user_input = input('Enter Your Number: ')
        if user_input == "":
            break
        num = int(user_input)
        user_num.append(num)
    return user_num

def count_num(lst):
    num_dict = {}
    for num in lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict  

def print_counts(num_dict):
    for num in num_dict:
        print(f'{num} appears {num_dict[num]} times.')

def main():
    user_nums = get_user_num()
    num_counts = count_num(user_nums)
    print_counts(num_counts)

if __name__ == '__main__':
    main()