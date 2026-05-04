"""
Write a Python program that takes a word as input from the user and checks whether it is a palindrome or not
"""
def palindrome_fun(word):

    if word == word[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


palindrome_fun(input("Input a word : "))
