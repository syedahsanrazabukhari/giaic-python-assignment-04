def main():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":        
    main()