from operator import truediv

# teststr = user input string to check for palindromes or exit


def is_palindrome(teststr):
    # Slice trick to reverst the string
    if teststr == teststr[::-1]:
        return True
    return False


run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit to quit the program"
    if teststr == "exit":
        run = False
        break

    # Convert the string to all lower case letters
    teststr = teststr.lower()

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", is_palindrome(newstr))
