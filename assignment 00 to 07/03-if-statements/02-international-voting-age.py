Peturksbouipo_age= 16
Stanlau_age = 25
Mayengua_age = 48

def main():
    user_age = int(input("Enter your age : "))


    if user_age >= Peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo_age}")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo_age}")


    if user_age >= Stanlau_age:
        print(f"You can vote in Stanlau where the voting age is {Stanlau_age}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau_age}")    


    
    if user_age >= Mayengua_age:
        print(f"You can vote in Mayengua where the voting age is {Mayengua_age}")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua_age}")     


if __name__ == "__main__":        
    main()