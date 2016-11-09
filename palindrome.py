while True:
    word = input("Please enter a word: ")
    word_reversed = ''.join(reversed(word))
    if word == word_reversed:
        print("That's a palindrome")

    else:
        print("This is not a palindrome")
