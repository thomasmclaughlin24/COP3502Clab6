# Name: Thomas McLaughlin

def encode(password):
    encoded_key = ''
    for i in range(len(password)
	altered_digit = int(password[i] + 3
        encoded_key += str(altered_digit)
    return encoded_key

if __name__ == '__main__':
    finished = False
    while not finished:
        print('\nMenu\n-------------\n'
              '1. Encode\n2. Decode\n'
              '3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print("The encoded password is " + encoded_password + ", and the original password is " + password + ".")
        elif option == 3:
            finished = True
