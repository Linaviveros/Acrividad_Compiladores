import sys
from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener

def main():
    input_stream = InputStream(sys.stdin.read())
    lexer = MiGramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiGramaticaParser(stream)
    tree = parser.programa()

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()
