def access_element(tools, index):
    try:
        return tools[index]
    except IndexError:
        return None

def modify_element(tools, index, value):
    try:
         tools[index] = value
         return tools
    except IndexError:    
        return None
    
def slice_list(tools, start, end):    
    try:
        return tools[start:end]
    except IndexError:
        return None

def main():
    tools = ["hammer", "screwdriver", "wrench", "tape", "drill"]
    print(f"Current tools: {tools}")
    print("Choose an operation: access, modify, slice")
    operation = input("Choose an operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(tools, index))
    elif operation == "modify":   
        index = int(input("Enter index to modify: "))
        value = input("Enter new value: ")
        print(modify_element(tools, index, value))
    elif operation == "slice":    
        index = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(tools, index, end))
    else:
        print("Invalid operation")    

if __name__ == "__main__":
    main()