# Function to get the word

def word():
    print("Please input your string:")

    text = input()

    return text


# Function to reverse the string

def reverseConversion():
    text = word()

    reversed_text = text[::-1]

    print(f"Reversed string: {reversed_text}")


def reverseiF():
    text = word()

    reverse = ""

    for char in text:
        reverse = char + reverse

    print(f"Reversed string: {reverse}")


# Call the function

reverseConversion()

reverseiF()

