#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha():
            result.append(str(ord(char) - 96))
    return ' '.join(result)
