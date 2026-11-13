def is_palindrome(text):
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    print(is_palindrome("Never odd or even"))
