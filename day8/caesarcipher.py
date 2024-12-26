alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
direction = input("Type 'encode to encode and 'decrypt' to decrypt: \n")
text = input("Type your message: \n")
shift = int(input("Type the shift number: \n"))

def encode(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        
        alphabets.index(letter)
        
        new_index= alphabets.index(letter) + shift_amount
        encrypted_text += alphabets[new_index]
    print(encrypted_text)
    
    
   
    

if direction == "encode":
    encode(text, shift)
    
# elif direction == "decrypt":
#     #text - shift
# else:
#     print("Please type either encode or decrypt")