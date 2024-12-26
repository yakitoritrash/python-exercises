alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
direction = input("Type 'encode to encode and 'decrypt' to decrypt: \n")
text = input("Type your message: \n")
shift = int(input("Type the shift number: \n"))

def encode(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabets:    
            alphabets.index(letter)
            
            new_index= (alphabets.index(letter) + shift_amount) % 26
            encrypted_text += alphabets[new_index]
        else:
            encrypted_text += letter
    print(encrypted_text)
  
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in alphabets:
            new_index = (alphabets.index(letter) - shift_amount) % 26
            decrypted_text += alphabets[new_index]
        else:
            encrypted_text += letter
    print(decrypted_text)
        
      
    
if direction == "encode":
    encode(text, shift)
    
elif direction == "decrypt":
    decrypt(text, shift)
else:
    print("Please type either encode or decrypt")