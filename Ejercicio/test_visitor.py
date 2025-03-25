import sys
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = MiGramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
