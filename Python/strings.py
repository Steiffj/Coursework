def main():
    greeting = "Salutations to everything I experience in my daily life and beyond!"
    greeting[-1]
    greeting[0] == greeting[0]
    greeting[-1] == greeting[len(greeting) - 1]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet[0:] == alphabet[:len(alphabet)]
    alphabet[2:4].upper() + " - a so-called compact disc. They don't seem so compact anymore...."
    alphabet == alphabet[::]
    alphabet[11::3].capitalize() + ", close to Lorax :)"
    alphabet[::-1]  # conventiently reverses a string
main()
