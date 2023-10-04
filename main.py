import re


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


def lexer(input_text):
    token_patterns = [
        ('keyword', r'while'),
        ('Separator', r'[(),;]'),
        ('Operator', r'[<=>]'),
        ('Real', r'\d+\.\d+'),
        ('Identifier', r'[a-zA-Z_]\w*'),
    ]

    validators = {
        'Identifier': identifier,
    }

    regex_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns)

    tokens = []

    for match in re.finditer(regex_pattern, input_text):
        token_type = match.lastgroup
        token_value = match.group()
        if token_type in validators:
            validator = validators[token_type]
            if not validator(token_value):
                raise ValueError(f"Invalid {token_type}: {token_value}")
        tokens.append((token_type, token_value))

    return tokens


if __name__ == '__main__':

    with open('input_scode.txt', 'r') as file:
        input_text = file.read()

    answer = "Token         Lexume\n"
    for pair in lexer(input_text):
        token = pair[0]
        lexume = pair[1]
        txt = "{:<14}{:<14}".format(token, lexume)
        answer += txt
        answer += "\n"

    with open("generated_tokens_lexemes.txt", "w") as output_file:
        output_file.write(answer)
