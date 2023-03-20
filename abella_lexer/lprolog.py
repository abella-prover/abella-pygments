from pygments.lexer import RegexLexer, inherit
from pygments.lexers.prolog import PrologLexer
from pygments.token import *

class LPrologLexer(PrologLexer):
    name = 'LProlog'
    aliases = ['lprolog', 'lambdaprolog'],
    filenames = ['*.sig', '*.mod']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\b(?:false|true)\b', Literal),
            (r'\b(?:pi|sigma|type|kind|sig|module|accum_sig|accumulate|is)\b', Keyword),
            (r'->', Keyword.Type),
            (r':-|-|=>|&|;|,|\^', Operator),
            (r'\b(o|string|list)\b', Keyword.Type),
            (r"\b(?:_+|[A-Z][A-Za-z0-9_'/-]*)", Name.Variable),
            (r"\b[a-z_][A-Za-z0-9_'/-]*", Name.Constant),
            (r'\\', Punctuation),
            inherit,
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\.', String.Escape),
            (r'[^"]+', String),
        ],
    }
