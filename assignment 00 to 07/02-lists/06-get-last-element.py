def get_last_element(last):
    print(last[-1])
def get_last():
       last= []
       elem: str = input("Please enter an element of the list or press enter to stop. ") 
       while elem != "":
             last.append(elem)
             elem = input("Please enter an element of the list or press enter to stop. ")
       return last     
def main():
      last_elements = get_last()
      get_last_element(last_elements)

if __name__ == "__main__":      
      main()