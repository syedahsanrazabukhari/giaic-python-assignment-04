def count_even_numbers(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    print(f"  There are {count} even numbers in the list you entered.")

def get_list_of_ints():
    list=[]
    user_input = input("Please enter an element of the list or press enter to stop. ")        
    while user_input != "":
        list.append(int(user_input))
        user_input = input("Please enter an element of the list or press enter to stop. ")
    return list

def main():
    lst =get_list_of_ints()
    count_even_numbers(lst)

if __name__ == "__main__":
    main()