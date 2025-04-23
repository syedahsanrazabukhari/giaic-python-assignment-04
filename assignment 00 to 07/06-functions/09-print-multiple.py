def print_multiple(msg,rep):
    for i in range(rep):
        print(msg)
def main():
    msg_input= input("Enter a message: ")
    rep_input= int(input("Enter a number do you want to repeat: "))
    print_multiple(msg_input,rep_input)
if __name__ == '__main__':
    main()  