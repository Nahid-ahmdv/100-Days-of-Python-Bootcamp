# def calculate_love_score(first_name, second_name):
#     combined_name = first_name.lower() + second_name.lower()
#     True_counter = 0
#     Love_counter = 0
#     for i in "true":
#         for j in combined_name:
#             if i == j:
#                 True_counter += 1
#     for i in "love":
#         for j in combined_name:
#             if i == j:
#                 Love_counter += 1
#     total_score = str(True_counter) + str(Love_counter)
#     print(int(total_score))

# calculate_love_score("Angela Yu", "Jack Bauer") #53
# calculate_love_score("Kanye West", "Kim Kardashian") #42
# calculate_love_score("Brad Pitt", "Jennifer Aniston") #73
# calculate_love_score("Prince William", "Kate Middleton") #67
# print("apple".index("le"))
# for i in "Type the shift number":
#     print(i, end = " ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text, shift_amount):
    new_text = ""
    for letter in original_text:
        if letter.isalpha():
            shifted_alphabet = alphabet.index(letter.lower()) + int(shift_amount)
            # if shifted_alphabet < len(alphabet):
            #     new_text += alphabet[shifted_alphabet]
            # else:
            #     new_text += alphabet[(shifted_alphabet - len(alphabet))]
            
            new_text += alphabet[(shifted_alphabet % len(alphabet))]

            # shifted_alphabet %= len(alphabet) #0_25
            # new_text += alphabet[shifted_alphabet]

        else:
            new_text += letter
    print(new_text)

encrypt("NahRddii Hellozy!", 3)
encrypt("dfghjncgjk,v", 7) #kmnoqujnqr
print(len(alphabet))

def decrypt(encrypted_text, shift_amount):
    decrypt_text = ""
    for letter in encrypted_text:
        if letter.isalpha():
            shifted_alphabet = alphabet.index(letter.lower()) - shift_amount
            shifted_alphabet %= len(alphabet) #0_25
            decrypt_text += alphabet[shifted_alphabet]
        else:
            decrypt_text += letter
    print(decrypt_text)



if direction.lower() == "encode":
    encrypt(original_text = text, shift_amount = shift)
if direction.lower() == "decode":
    decrypt(encrypted_text = text, shift_amount = shift)