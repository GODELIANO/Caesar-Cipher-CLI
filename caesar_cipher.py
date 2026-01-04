def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(),
                                     shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)
    

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def get_shift():
    while True:
        raw = input("Shift (1-25): ").strip()
        try:
            shift = int(raw)
        except ValueError:
            print("Shift must be an integer value.")
            continue  # <-- fondamentale

        if 1 <= shift <= 25:
            return shift
        
        print("Shift must be an integer between 1 and 25.")


def main():
    action = input("Action (encrypt/decrypt): ").strip().lower()
    while action not in ("encrypt", "decrypt", "e", "d"):
        action = input("Please type 'encrypt' or 'decrypt' (e/d): ").strip().lower()
    
    text = input("Text: ")
    shift = get_shift()

    if action in ("encrypt", "e"):
        result = encrypt(text, shift)
        print("\nEncrypted text:")
        print(result)
    else:
        result = decrypt(text, shift)
        print("\nDecrypted text:")
        print(result)


if __name__ == "__main__":
    main()
