from ast import *


class NotAllowed(Exception):
    def __init__(self, operation):
        self.op = operation

    def __str__(self):
        return "NotAllowed(", self.op, ")"


def NA(operation):
    raise NotAllowed


class BaseGenerator(NodeVisitor):

    def __init__(self, indent_with, add_line_information=False):
        self.result = []
        self.indent_with = indent_with
        self.add_line_information = add_line_information
        self.indentation = 0
        self.new_lines = 0

    def write(self, x):
        if self.new_lines:
            if self.result:
                self.result.append('\n' * self.new_lines)
            self.result.append(self.indent_with * self.indentation)
            self.new_lines = 0
        self.result.append(x)

    def newline(self, node=None, extra=0):
        self.new_lines = max(self.new_lines, 1 + extra)
        if node is not None and self.add_line_information:
            self.write('# line: %s' % node.lineno)
            self.new_lines = 1

    def body(self, statements):
        self.new_line = True
        self.indentation += 1
        for stmt in statements:
            self.visit(stmt)
        self.indentation -= 1

    def body_or_else(self, node):
        self.body(node.body)
        if node.orelse:
            self.newline()
            self.write('else:')
            self.body(node.orelse)

    def signature(self, node):
        want_comma = []
        def write_comma():
            if want_comma:
                self.write(', ')
            else:
                want_comma.append(True)

        padding = [None] * (len(node.args) - len(node.defaults))
        for arg, default in zip(node.args, padding + node.defaults):
            write_comma()
            self.visit(arg)
            if default is not None:
                self.write('=')
                self.visit(default)
        if node.vararg is not None:
            write_comma()
            self.write('*' + node.vararg)
        if node.kwarg is not None:
            write_comma()
            self.write('**' + node.kwarg)

    def decorators(self, node):
        for decorator in node.decorator_list:
            self.newline(decorator)
            self.write('@')
            self.visit(decorator)

    def visit_Assert(self, node):
        NA("assertions")

    def visit_ImportFrom(self, node):
        NA("imports")

    def visit_Import(self, node):
        NA("imports")

    def visit_With(self, node):
        NA("with")

    def visit_Pass(self, node):
        NA("pass")

    def visit_Print(self, node):
        NA("print")

    def visit_TryExcept(self, node):
        NA("exceptions")

    def visit_TryFinally(self, node):
        NA("exceptions")

    def visit_Global(self, node):
        NA("fancy scopes")

    def visit_Nonlocal(self, node):
        NA("fancy scopes")

    def visit_Continue(self, node):
        NA("continue")

    def visit_Tuple(self, node):
        NA("tuples")

    def visit_Yield(self, node):
        NA("yield")

    def visit_Lambda(self, node):
        NA("lambdas")

    def visit_Ellipsis(self, node):
        NA("ellipsis")

    def visit_ListComp(self, node):
        NA("comprehensions")

    def visit_GeneratorExp(self, node):
        NA("comprehensions")

    def visit_SetComp(self, node):
        NA("comprehensions")

    def visit_DictComp(self, node):
        NA("comprehensions")

    def visit_Starred(self, node):
        NA("*starred")

    def visit_Repr(self, node):
        NA("repr")

    def visit_alias(self, node):
        NA("aliases")

    def visit_comprehension(self, node):
        NA("comprehensions")

    def visit_excepthandler(self, node):
        NA("exceptions")

    def visit_For(self, node):
        NA("for")

    def visit_While(self, node):
        NA("while")

    def visit_Delete(self, node):
        NA("delete")

    def visit_Return(self, node):
        NA("return")
