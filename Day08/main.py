import art
print(art.logo) #ASCII art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(dir, user_text, shift_amount):
    new_text = ""
    if dir.lower() == "decode":
        shift_amount *= -1
    for letter in user_text:
        if letter.isalpha():
            shifted_alphabet = alphabet.index(letter.lower()) + shift_amount
            # elif dir.lower() == "decode":
            #     shifted_alphabet = alphabet.index(letter.lower()) - shift_amount  
            shifted_alphabet %= len(alphabet) #0_25
            new_text += alphabet[shifted_alphabet]
        else:
            new_text += letter
    print(f"Here is the {dir}d result: {new_text}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(dir = direction, user_text = text, shift_amount = shift)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if restart.lower() == 'yes':
        continue
    else:
        print("Goodbye then!")
        break
    



# def encrypt(original_text, shift_amount):
#     new_text = ""
#     for letter in original_text:
#         if letter.isalpha():
#             shifted_alphabet = alphabet.index(letter.lower()) + shift_amount
#             shifted_alphabet %= len(alphabet) #0_25
#             new_text += alphabet[shifted_alphabet]
#         else:
#             new_text += letter
#     print(new_text)

# def decrypt(encrypted_text, shift_amount):
#     decrypt_text = ""
#     for letter in encrypted_text:
#         if letter.isalpha():
#             shifted_alphabet = alphabet.index(letter.lower()) - shift_amount
#             shifted_alphabet %= len(alphabet) #0_25
#             decrypt_text += alphabet[shifted_alphabet]
#         else:
#             decrypt_text += letter
#     print(decrypt_text)



# if direction.lower() == "encode":
#     encrypt(original_text = text, shift_amount = shift)
# if direction.lower() == "decode":
#     decrypt(encrypted_text = text, shift_amount = shift)