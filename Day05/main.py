letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

def PyPassword_Generator(nlet, nsymb, nnumb):
    password = ""
    for i in range(0, nlet):
        password += letters[random.randint(0, len(letters)-1)]
    for i in range(0, nsymb):
        # isymb += symbols[random.randint(0, len(symbols)-1)]
        password += random.choice(symbols)
    for i in range(0, nnumb):
        password += numbers[random.randint(0, len(numbers)-1)]
    # print(ilet + isymb + inumb)
    password_list = list(password)
    random.shuffle(password_list)
    # b = ''.join(random.shuffle(password_list)) #random.shuffle() modifies (updates) the list in place and returns None. You are doing random.shuffle(password_list), which returns None, and then trying to ''.join(None), which will cause an error.
    b = ''.join(password_list)
    return f"{password}\n{b}"  # Returning as a formatted string

b = PyPassword_Generator(nr_letters, nr_symbols, nr_numbers)
print(b)


# n = ["s", "g", "h"]
# print(''.join(n))
#output: sgh

# n = "hello"
# s = list(n)
# print(s)
#output: ['h', 'e', 'l', 'l', 'o']