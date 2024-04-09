text = input("Enter a text: ")
option = int(input("Enter either 1 to encript or 2 to descript: "))

cypher_text = ''

for letter in text:
    if letter == ' ':
        cypher_text += ' '
        continue
    if option == 1:
        if ord(letter) >= ord('x'):
            cypher_text += chr(ord(letter) - 26 + 3)
        else:    
            cypher_text += chr(ord(letter) + 3)
    else:
        if ord(letter) <= ord('c'):
            cypher_text += chr(ord(letter) + 26 - 3)
        else:    
            cypher_text += chr(ord(letter) - 3)
print(cypher_text)
