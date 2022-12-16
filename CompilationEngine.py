"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import typing

T_types_dic = {"INT_CONST": "integerConstant", "SYMBOL": "symbol",
               "IDENTIFIER": "identifier", "KEYWORD": "keyword",
               "STRING_CONST": "stringConstant"}

keyWords = \
    {'boolean': 'BOOLEAN', 'char': 'CHAR', 'class': 'CLASS',
     'constructor': 'CONSTRUCTOR', 'do': 'DO', 'else': 'ELSE',
     'false': 'FALSE', 'field': 'FIELD', 'function': 'FUNCTION', 'if': 'IF',
     'int': 'INT', 'let': 'LET', 'method': 'METHOD', 'null': 'NULL',
     'return': 'RETURN', 'static': 'STATIC', 'this': 'THIS', 'true': 'TRUE',
     'var': 'VAR', 'void': 'VOID', 'while': 'WHILE'}

symbols = \
    {'&', '(', ')', '*', '+', ',', '-', '.', '/', ';', '<', '=', '>', '[', ']',
     '{', '|', '}', '~'}

keyword_switch = \
    {'BOOLEAN': 'boolean', 'CHAR': 'char', 'CLASS': 'class',
     'CONSTRUCTOR': 'constructor', 'DO': 'do', 'ELSE': 'else',
     'FALSE': 'false', 'FIELD': 'field', 'FUNCTION': 'function', 'IF': 'if',
     'INT': 'int', 'LET': 'let', 'METHOD': 'method', 'NULL': 'null',
     'RETURN': 'return', 'STATIC': 'static', 'THIS': 'this', 'TRUE': 'true',
     'VAR': 'var', 'VOID': 'void', 'WHILE': 'while'}

symbol_switch = \
    {'&': '&amp;', '(': '(', ')': ')', '*': '*', '+': '+', ',': ',', '-': '-',
     '.': '.', '/': '/', '\"': '', ';': ';', '<': '&lt;', '=': '=',
     '>': '&gt;', '[': '[', ']': ']', '{': '{', '|': '|', '}': '}', '~': '~'}

op_list = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
unary_op_list = ['-', '~']
keyword_constant = ["TRUE", "FALSE", "NULL", "THIS"]


class CompilationEngine:
    """Gets input from a JackTokenizer and emits its parsed structure into an
    output stream.
    """

    def compile_token(self):
        token, token_type = self.get_token(), \
                            self.JackTokenizer.token_type()
        self.os.write(f"<{token}>")

        self.os.write(f"</{token}>")

    def __init__(self, input_stream: "JackTokenizer", output_stream) -> None:
        """
        Creates a new compilation engine with the given input and output. The
        next routine called must be compileClass()
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        """
        self.token, self.token_type = "", ""
        self.JackTokenizer = input_stream
        self.os = output_stream
        self.spaces = ""
        pass

    def compile_class(self) -> None:
        """Compiles a complete class."""
        pass

    def compile_class_var_dec(self) -> None:

        """Compiles a static declaration or a field declaration."""
        # Your code goes here!

        words_list, types_list = [], []
        self.open_main_xml("classVarDec")
        self.add_spaces()
        self.print_and_advance()
        self.print_and_advance()

        while self.get_token() != ";" and self.JackTokenizer.has_more_tokens():
            self.add_type_and_token(words_list, types_list)
            self.advance()

        for idx, word in enumerate(words_list):
            self.print_to_file(
                f"<{T_types_dic[types_list[idx]]}> {word} </{T_types_dic[types_list[idx]]}>\n")

        self.remove_spaces()
        self.close_main_xml("classVarDec")

    def compile_subroutine(self) -> None:
        """
        Compiles a complete method, function, or constructor.
        You can assume that classes with constructors have at least one field,
        you will understand why this is necessary in project 11.
        """
        # Your code goes here!
        pass

    def compile_parameter_list(self) -> None:
        """Compiles a (possibly empty) parameter list, not including the
        enclosing "()".
        """
        # Your code goes here!
        pass

    def compile_var_dec(self) -> None:
        words_list, types_list = [], []
        self.open_main_xml("varDec")
        self.add_spaces()
        self.print_and_advance()
        self.print_and_advance()

        while self.get_token() != ";" and self.JackTokenizer.has_more_tokens():
            self.add_type_and_token(words_list, types_list)
            self.advance()

        for idx, word in enumerate(words_list):
            self.print_to_file(
                f"<{T_types_dic[types_list[idx]]}> {word} </{T_types_dic[types_list[idx]]}>\n")

        self.remove_spaces()
        self.close_main_xml("varDec")
        # Your code goes here!

    def compile_statements(self) -> None:
        """Compiles a sequence of statements, not including the enclosing
        "{}".
        """
        # Your code goes here!
        pass

    def compile_do(self) -> None:
        """Compiles a do statement."""
        self.open_main_xml("doStatement")
        self.add_spaces()
        while self.get_token() != ';':
            self.print_and_advance()
        self.remove_spaces()
        self.close_main_xml("doStatement")

    def compile_let(self) -> None:
        """Compiles a let statement."""
        self.open_main_xml("letStatement")
        while self.get_token() != ';':
            self.print_and_advance()
        self.close_main_xml("letStatement")
        # TODO

    def compile_while(self) -> None:
        """Compiles a while statement."""
        # Your code goes here!
        pass

    def compile_return(self) -> None:
        """Compiles a return statement."""
        self.print_to_file("<returnStatement>\n")
        self.add_spaces()
        self.print_and_advance()
        self.print_and_advance()
        self.remove_spaces()
        self.print_to_file("</returnStatement>\n")

    def compile_if(self) -> None:
        """Compiles a if statement, possibly with a trailing else clause."""
        # Your code goes here!
        pass

    def compile_expression(self) -> None:
        """Compiles an expression."""
        # Your code goes here!
        pass

    def compile_term(self) -> None:
        """Compiles a term.
        This routine is faced with a slight difficulty when
        trying to decide between some of the alternative parsing rules.
        Specifically, if the current token is an identifier, the routing must
        distinguish between a variable, an array entry, and a subroutine call.
        A single look-ahead token, which may be one of "[", "(", or "." suffices
        to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        # Your code goes here!
        self.open_main_xml("term")
        self.add_spaces()
        self.advance()
        token_type, token = self.JackTokenizer.token_type(), self.get_token()
        if token_type == "INT_CONST":
            self.print_int_constant()
        elif token_type == "STRING_CONST":
            self.print_str_constant()
        elif token_type == "KEYWORD" and token in keyword_constant:
            self.print_keyword_constant()
        # 1. לבדוק האם מדובר בפותח או סוגר או נקודה
        # 2. אם פותחים יש צורך לקרוא לאספרישן.
        # 3. אם סוגרים סיימנו טרם
        # 4. יש אופציה לסוגרים ואז אונארי ואז טרם
        # 5. יכול לבוא ספרוטין קול במקרה של סוגריים
        # 6. כלומר במקרה של סוגריים נצטרך לבוק מה יש בפנים
        self.close_main_xml("term")

    def compile_expression_list(self) -> None:
        """Compiles a (possibly empty) comma-separated list of expressions."""
        # Your code goes here!
        pass

    # **************************** helper functions ***************************

    def add_type_and_token(self, tokens_list, types_list):
        tokens_list.append(self.get_token())
        types_list.append(self.JackTokenizer.token_type())

    def add_spaces(self):
        self.spaces += "  "

    def remove_spaces(self):
        self.spaces = self.spaces[:-2]

    def print_to_file(self, txt: str):
        self.os.write(self.spaces + txt)

    def print_and_advance(self):
        token = self.get_token()  # add 'field'
        token_type = self.JackTokenizer.token_type()
        self.advance()
        self.os.write(
            self.spaces + f"<{T_types_dic[token_type]}> {token} </{T_types_dic[token_type]}>\n")

    def open_xml(self, txt):
        self.os.write(self.spaces + f"<{txt}>")

    def close_xml(self, txt):
        self.open_xml('/' + txt)

    def open_main_xml(self, txt):
        self.open_xml(txt)
        self.down_line()

    def close_main_xml(self, txt):
        self.open_xml(txt)
        self.down_line()

    def term_type(self):
        # "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
        token_type = self.JackTokenizer.token_type()
        if token_type in ["INT_CONST", "STRING_CONST"]:
            return token_type

    def print_int_constant(self):
        self.open_xml("integerConstant")
        self.os.write(self.spaces + f"{self.JackTokenizer.int_val()}")
        self.close_xml("integerConstant")

    def print_str_constant(self):
        self.open_xml("stringConstant")
        self.os.write(self.spaces + f"{self.JackTokenizer.string_val()}")
        self.close_xml("stringConstant")

    def print_keyword_constant(self):
        self.open_xml("keyword")
        self.os.write(self.spaces + f"{keyword_switch[self.JackTokenizer.keyword()]}")
        self.close_xml("keyword")

    def down_line(self):
        self.close_xml("\n")

    def get_token(self):
        return self.JackTokenizer.get_token()

    def get_type(self):
        return self.JackTokenizer.get_type()

    def advance(self):
        self.JackTokenizer.advance()
