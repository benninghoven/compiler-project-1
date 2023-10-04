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


# Check if is valid variable or digit
def identifier(input_str):
    state = 0
    for char in input_str:
        if state == 0:
            if is_digit(char):
                state = 1
            elif is_identifier_start(char):
                state = 2
            else:
                return None
        elif state == 1:
            if is_digit(char):
                continue
            else:
                return None
        elif state == 2:
            if is_identifier_char(char):
                continue
            else:
                return None

    if state == 1:  # integer
        return True
    elif state == 2:  # identifier
        return True
