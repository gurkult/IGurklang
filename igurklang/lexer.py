from typing import Iterator
from gurklang.parser import tokenizer
from pygments.lexer import Lexer
import pygments.token as t


_TOK_PYGMENTS_MAP = {
    'LEFT_PAREN': t.Punctuation,
    'RIGHT_PAREN': t.Punctuation,
    'LEFT_BRACE': t.Operator,
    'RIGHT_BRACE': t.Operator,
    'INT': t.Number,
    'STRING': t.String,
    'ATOM': t.Name.Decorator,
    'NAME': t.Name.Namespace,
    'WHITESPACE': t.Whitespace,
    'COMMENT': t.Comment,
}


class GurkLexer(Lexer):

    mimetypes=['text/gurklang']
    filenames=['*.gurk']
    name = 'gurklang lexer'
    aliases = ['gurklang', 'py-gurklang']

    def get_tokens_unprocessed(self, text: str) -> Iterator[tuple[int, t._TokenType, str]]:
        for token in tokenizer.tokenize_with_ignored(text):
            pos = token.position
            value = token.value
            tok_type = _TOK_PYGMENTS_MAP[token.name]
            yield pos, tok_type, value