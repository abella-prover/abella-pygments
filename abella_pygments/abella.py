from pygments.lexer import RegexLexer, inherit, bygroups, using
from pygments.token import *

from .lprolog import LPrologLexer

class AbellaSpecLexer(LPrologLexer):
    tokens = {
        'root': [
            (r'\[|\]|\|-', Punctuation),
            (r'olist', Keyword.Type),
            inherit
        ]
    }

class AbellaLexer(LPrologLexer):
    name = 'Abella'
    aliases = ('abella',)
    filenames = ('*.thm',)

    tokens = {
        'root': [
            (r'\s+', Whitespace),
            (r'({)([^}]*)(})', bygroups(Punctuation,using(AbellaSpecLexer),Punctuation)),
            (r'"(?:\\"|[^\\"])*"', String),
            (r':=', Punctuation),
            (r'/\\|\\/', Operator),
            (r'\d+', Number.Integer), # no floating point numbers plz
            (r'\b(?:prop|o|olist)\b', Keyword.Type),
            (r'\b(?:true|false)\b', Keyword.Constant),
            (r'\b(?:forall|exists|nabla)\b', Keyword),
            (r'\b(?:Set|Query|Show)\b', Keyword),
            (r'\b(?:Import|Specification|as)\b', Keyword),
            (r'\b(?:Type|Kind|Close)\b', Keyword.Declaration),
            (r'\b(?:Define|CoDefine|Recursive|Inductive|by)\b', Keyword.Declaration),
            (r'\b(?:Theorem|Split)\b', Keyword.Declaration),
            (r'\b(?:skip|undo|abort)\b', Generic.Error),
            (r'\b(?:abbrev|all|apply|assert|backchain|case|clear|coinduction|cut|induction|inst|intros|keep|left|monotone|on|permute|rename|right|search|split\*?|to|unabbrev|unfold|with|witness)\b', Name.Function),
            (r'/\*', Comment, 'nested-comment'),
            inherit,
        ],
        'nested-comment': [
            (r'/\*', Comment, '#push'),
            (r'\*/', Comment, '#pop'),
            (r'[^*/]+', Comment),
            (r'[*/]', Comment),
        ],
    }
