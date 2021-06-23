logo = """
.___  ___.   ______   .______          _______. _______      ______   ______    _______   _______ 
|   \/   |  /  __  \  |   _  \        /       ||   ____|    /      | /  __  \  |       \ |   ____|
|  \  /  | |  |  |  | |  |_)  |      |   (----`|  |__      |  ,----'|  |  |  | |  .--.  ||  |__   
|  |\/|  | |  |  |  | |      /        \   \    |   __|     |  |     |  |  |  | |  |  |  ||   __|  
|  |  |  | |  `--'  | |  |\  \----.----)   |   |  |____    |  `----.|  `--'  | |  '--'  ||  |____ 
|__|  |__|  \______/  | _| `._____|_______/    |_______|    \______| \______/  |_______/ |_______|
"""

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..', '9':'----.',
                   '0':'-----', ', ':'--..--', '.':'.-.-.-',
                   '?':'..--..', '/':'-..-.', '-':'-....-',
                   '(':'-.--.', ')':'-.--.-'}

MORSE_CODE_REVERSED = {value:key for key,value in MORSE_CODE_DICT.items()}

def encrypt(text):
    morse_code = ""
    words = text.split(" ")
    for word in words:
        for char in word:
            morse_code += MORSE_CODE_DICT[char] + " "
    return morse_code

def decrypt(morse_code):
    text = ""
    for code in morse_code.split():
        text += MORSE_CODE_REVERSED.get(code)
    return text


print(logo)

game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode":
        text = input("Enter text to convert to Morse Code: \n").upper()
        print(encrypt(text))
    elif direction == "decode":
        morse_code = input("Enter morse code to convert to normal text: \n")
        print(decrypt(morse_code))
    else:
        print("Wrong Code!")
    game_continued = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if game_continued == 'yes':
        game_on = True
    elif game_continued == "no":
        game_on = False
        print("Good Bye!")
