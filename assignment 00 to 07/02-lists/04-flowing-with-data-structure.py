def add_three_copies(mylist, mydata):
    for i in range(3):
        mylist.append(mydata)

def main():
        user_msg= input("Please enter your message to copy :")
        mylist = []
        print("Print list before", mylist )
        add_three_copies(mylist, user_msg)
        print("Print list after", mylist )

if __name__ == "__main__":
  main()