#!/usr/bin/python

from ast import *
from generators.java import JavaGenerator
from generators.python import PythonGenerator


def to_source(node, cls=PythonGenerator, indent_with=' ' * 4, add_line_information=False):
    """This function can convert a node tree back into python sourcecode.
    This is useful for debugging purposes, especially if you're dealing with
    custom asts not generated by python itself.

    It could be that the sourcecode is evaluable when the AST itself is not
    compilable / evaluable.  The reason for this is that the AST contains some
    more data than regular sourcecode does, which is dropped during
    conversion.

    Each level of indentation is replaced with `indent_with`.  Per default this
    parameter is equal to four spaces as suggested by PEP 8, but it might be
    adjusted to match the application's styleguide.

    If `add_line_information` is set to `True` comments for the line numbers
    of the nodes are added to the output.  This can be used to spot wrong line
    number information of statement nodes.
    """
    generator = cls(indent_with, add_line_information)
    generator.visit(node)

    return ''.join(generator.result)


if __name__ == '__main__':
    source = open("source.py.txt", "r").read()
    parsed = parse(source)
    print('\nPYTHON')
    print(''.join(to_source(parsed, cls=PythonGenerator)))
    print('\nJAVA')
    print(''.join(to_source(parsed, cls=JavaGenerator)))
