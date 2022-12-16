"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import os
import sys
import typing
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer

T_types_dic = {"INT_CONST": "integerConstant", "SYMBOL": "symbol",
               "IDENTIFIER": "identifier","KEYWORD": "keyword",
               "STRING_CONST": "stringConstant"}


def analyze_file(
        input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """Analyzes a single file.

    Args:
        input_file (typing.TextIO): the file to analyze.
        output_file (typing.TextIO): writes all output to this file.
    """
    # Your code goes here!
    tokenizer = JackTokenizer(input_file)
    engine = CompilationEngine(tokenizer, output_file)
    # "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST"
    # print("<tokens>")
    # while tokenizer.has_more_tokens():
    #     # engine.compile_token()
    #     type = tokenizer.token_type()
    #     token = tokenizer.get_token()
    #     if token =="<":
    #         token="&lt;"
    #     elif token ==">":
    #         token="&gt;"
    #     elif token =="&":
    #         token="&amp;;"
    #     if type == "STRING_CONST":
    #         token=token[1:-1]
        # print(f"<{T_types_dic[type]}> {token} </{T_types_dic[type]}>")
    # 
    #     tokenizer.advance()
    # print("</tokens>")
    engine.compile_var_dec()
    engine.JackTokenizer.advance()
    engine.compile_var_dec()


if "__main__" == __name__:
    # Parses the input path and calls analyze_file on each input file.
    # This opens both the input and the output files!
    # Both are closed automatically when the code finishes running.
    # If the output file does not exist, it is created automatically in the
    # correct path, using the correct filename.
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: JackAnalyzer <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".jack":
            continue
        output_path = filename + ".xml"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            analyze_file(input_file, output_file)
