# compiler-project-1
# CPSC 323 Compilers & Languages (Fall 2023) - Project 1

**Deadline:** Oct 4th, 2023

The first project assignment is to write a lexical analyzer (Lexer). Lexical analysis is the process of reading the stream of characters making up the source code of a program and dividing the input into tokens.

## Lexer

In this project, you will be required to write a procedure (Function) called `lexer()` that returns a token when it's required. Your `lexer()` function should return a record with two fields: one for the token and one for the token's actual "value" (lexeme), or the instance of a token.

## Getting Started

To begin the project, follow these steps:

1. Design and implement Finite State Automata (FSA) for the following tokens: identifier and integer. The rest can be written ad-hoc. Deductions will occur if this step is not followed.
2. Write regular expressions (REs) and draw the FSA for the required tokens (identifier and integer) and put them in a document named "FSA_mydesign.doc".
3. Develop an executable program using C/C++/Java/Python that implements your lexer. Use the `lexer()` method to read and return subsequent tokens.
4. Print out the results into two columns: one for tokens and another for lexemes. Save this information in a document named "output" (example input/output format provided below).
5. Create a "readme" file to provide brief documentation and instructions on how to set up and run your program if needed.

## Submission

Your submission must consist of five (5) files:

1. The provided "input_scode.txt" file containing the source code.
2. "FSA_mydesign.doc" document with your FSA designs.
3. Your program file developed in C/C++/Java/Python.
4. An "output" file with the generated tokens and lexemes.
5. This "readme.md" file specifying project details and setup instructions.

## Example Input/Output

**Input Source code (input_scode.txt):**
```plaintext
while (t < upper) s = 22.00;

Output

Token         Lexeme
keyword       while
Separator     (
Identifier     t
Operator      <
Identifier     upper
Separator     )
Identifier     s
Operator      =
Real          22.00
Separator     ;

Please ensure your program reads "input_scode.txt" and generates output in a similar format.

Note: The project description provided here is a brief summary. Refer to the detailed project instructions for further information and requirements. Good luck with your project!


