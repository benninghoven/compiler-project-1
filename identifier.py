def is_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'


def is_digit(char):
    return '0' <= char <= '9'


def is_underscore(char):
    return char == '_'


def is_identifier_start(char):
    return is_letter(char) or is_underscore(char)


def is_identifier_char(char):
    return is_letter(char) or is_digit(char) or is_underscore(char)


# Check if is valid variable name or digit
def identifier(input_str):
    state = 0
    identifier = ""

    for char in input_str:
        if state == 0:
            if is_identifier_start(char):
                state = 1
                identifier += char
            else:
                return None  # Invalid input
        elif state == 1:
            if is_identifier_char(char):
                identifier += char
            else:
                return identifier  # Identifier recognized
    return identifier
