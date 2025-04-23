def num_in_stock (fruite):
    if fruite == 'apple':
      return 7
    if fruite == 'banana':
      return 3
    if fruite == 'kiwi':
      return 5
    if fruite == 'mango':
       return 119
    if fruite == 'orange':
       return 10
    if fruite == 'pineapple':
       return 2
    return 0
def main():
   fruite = input("Enter Fruite: ")
   stock = num_in_stock(fruite)
   if stock > 0:
     print(f"{fruite} is in stock. There are {stock} left.")
   else:
     print(f"{fruite} is not in stock.")

if __name__ == '__main__':
   main()