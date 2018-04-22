ILLEGAL = "ILLEGAL"
EOF     = "EOF"

// Identifiers + literals
IDENT = "IDENT" // add, foobar, x, y, ...
INT   = "INT"   // 1343456

// Operators
ASSIGN   = "="
PLUS     = "+"

// Delimiters
COMMA     = ","
SEMICOLON = ";"

LPAREN = "("
RPAREN = ")"
LBRACE = "{"
RBRACE = "}"

// Keywords
FUNCTION = "FUNCTION"
LET      = "LET"


# Presently, Token is only a guess. I am at the very start of the book. I
# don't know Go, so cannot be confident in my prediction about what python
# code will best express the intent of the Go. It *does* seem a bit
# heavyweight to have a class, but the Go uses a struct and in general when C
# does a struct, it seems likely to be a class in Python. Though, I might want
# to consider a named tuple. ThinkMore

class Token():
    def __init__(self, type, token):
        self.type = type
        self.token = token

