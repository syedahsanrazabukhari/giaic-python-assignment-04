min_height : int = 50 

def main():
    while True:  # Infinite loop, jab tak user khaali input nahi deta
        height_input = input("How tall are you? (Press Enter to stop) ")
        
        if height_input == "":  # Agar input khaali ho
            print("Goodbye!")  # Farewell message
            break  # Program stop kar denge
            
        height = float(height_input)  # Convert height to float
        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()