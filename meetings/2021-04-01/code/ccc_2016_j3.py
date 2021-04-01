text = input()
longest_len = 0


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


for start_index in range(0, len(text)):
    for end_index in range(len(text), start_index, -1):
        substr = text[start_index:end_index]
        if is_palindrome(substr):
            substr_len = len(substr)
            if len(substr) > longest_len:
                longest_len = substr_len

print(longest_len)
