# Alisha Chowdhury, group 44

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3) # shifting the numbers up by 3
        encoded_password += str(new_digit) # creating the encoded password
    return encoded_password

def main():
    encoded_password = ""

    while True: # creates the menu
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        print("Please enter an option:", end=" ")
        option = input()

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit(): # checks to see if entered password is 8 digits and only numbers, if not, prints invalid message
                encoded_password = encode(password)
                print("Your password has been encoded and stored!\n")
            else:
                print("Invalid password.\n")
        elif option == "2":
            # decode option from partner (cole ronkin)
            # start partner code here:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.\n")
        elif option == "3":
            break

if __name__ == "__main__":
    main()
