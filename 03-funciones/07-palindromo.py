def is_palindrome(text: str) -> bool:

    text_lower = text.lower()
    text_lower_without_spaces = text_lower.replace(" ", "")
    # print(f"formated text: {text_lower_without_spaces}")

    text_length = len(text_lower_without_spaces)
    index = text_length
    new_text = ""
    while index > 0:
        new_text += text_lower_without_spaces[index - 1]
        index -= 1

    # print(f"{text_lower_without_spaces} {new_text}")

    return text_lower_without_spaces == new_text


print(f"reconocer:\t\t{is_palindrome("reconocer")}")
print(f"amor:\t\t{is_palindrome("amor")}")
print(f"anilina:\t\t{is_palindrome("anilina")}")
print(f"amo la paloma:\t\t{is_palindrome("amo la paloma")}")
print(f"pedro:\t\t{is_palindrome("pedro")}")
