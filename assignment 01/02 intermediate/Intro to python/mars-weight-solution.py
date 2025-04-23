def main():
    lanet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
    }
    weight = float(input("Enter your weight: "))
    planet = input("Enter the name of a planet: ")
    if planet in lanet_gravity:
        palanet_weight = weight * lanet_gravity[planet]
        print(f"Your weight on {planet} is {palanet_weight}.")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

if __name__ == "__main__":
    main()