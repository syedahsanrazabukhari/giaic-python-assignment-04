def main():
     fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
     total_price = 0
     for fruit, price in fruits.items():
          quantity = int(input(f"Enter the quantity of {fruit} (in kilograms): "))
          total_price += quantity * price
     print("Your total is $" + str(total_price))
if __name__ == '__main__':
     main()