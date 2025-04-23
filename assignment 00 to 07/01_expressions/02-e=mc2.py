C: int = 299792458 


def main():
    mass_in_kg: float = float(input("Enter mass in kg :"))
    energy_in_joules = mass_in_kg * C**2
    print("e = m * C^2 ")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(f"Energy in joules: {energy_in_joules}")

if __name__ == "__main__":
    main()