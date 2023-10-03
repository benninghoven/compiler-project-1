from identifier import identifier

KEYWORD = 'keyword'
IDENTIFIER = 'identifier'
OPERATOR = 'operator'
REAL = 'real'
SEPARATOR = 'separator'

keyword_pattern = r'while|if|else|...'  # Add more keywords
identifier_pattern = r'[a-zA-Z_]\w*'
operator_pattern = r'[+\-*/=<>]'
real_pattern = r'\d+\.\d+'
separator_pattern = r'[();]'

token_patterns = [
    (keyword_pattern, KEYWORD),
    (identifier_pattern, IDENTIFIER),
    (operator_pattern, OPERATOR),
    (real_pattern, REAL),
    (separator_pattern, SEPARATOR),
]


def lexer(input):
    token = ""
    lexume = input
    return (token, lexume)


if __name__ == '__main__':

    with open('input_scode.txt', 'r') as file:
        input_code = file.read()

    for input in input_code.split():
        tokenLexumeTuple = lexer(input)
        print("token:", tokenLexumeTuple[0], "lexume:", tokenLexumeTuple[1])

    temp = lexer(input_code)

    with open("generated_tokens_lexemes.txt", "w") as output_file:
        output_file.write("test\n")
