max_len = 3

def get_shorten(lst):
    while len(lst) > max_len:
         last_elem = lst.pop()
         print(last_elem)

def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def mian():
      lst = get_lst()
      get_shorten(lst)


if __name__ == '__main__':      
      mian()