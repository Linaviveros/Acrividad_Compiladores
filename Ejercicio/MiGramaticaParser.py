# Generated from MiGramatica.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("Y\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\5\4+\n\4\7\4-\n\4\f\4\16\4\60\13\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tL\n\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\7\tT\n\t\f\t\16\tW\13\t\3\t\2")
        buf.write("\3\20\n\2\4\6\b\n\f\16\20\2\5\3\2\n\r\3\2\16\17\3\2\20")
        buf.write("\21\2X\2\25\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b\63\3\2")
        buf.write("\2\2\n\67\3\2\2\2\f;\3\2\2\2\16?\3\2\2\2\20K\3\2\2\2\22")
        buf.write("\23\5\4\3\2\23\24\7\3\2\2\24\26\3\2\2\2\25\22\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2")
        buf.write("\2\31\32\7\2\2\3\32\3\3\2\2\2\33\36\5\6\4\2\34\36\5\16")
        buf.write("\b\2\35\33\3\2\2\2\35\34\3\2\2\2\36\5\3\2\2\2\37 \7\4")
        buf.write("\2\2 !\7\5\2\2!\"\5\b\5\2\"#\7\3\2\2#$\5\n\6\2$%\7\3\2")
        buf.write("\2%&\5\f\7\2&\'\7\6\2\2\'.\7\7\2\2(*\5\4\3\2)+\7\3\2\2")
        buf.write("*)\3\2\2\2*+\3\2\2\2+-\3\2\2\2,(\3\2\2\2-\60\3\2\2\2.")
        buf.write(",\3\2\2\2./\3\2\2\2/\61\3\2\2\2\60.\3\2\2\2\61\62\7\b")
        buf.write("\2\2\62\7\3\2\2\2\63\64\7\22\2\2\64\65\7\t\2\2\65\66\5")
        buf.write("\20\t\2\66\t\3\2\2\2\678\7\22\2\289\t\2\2\29:\7\23\2\2")
        buf.write(":\13\3\2\2\2;<\7\22\2\2<=\7\t\2\2=>\5\20\t\2>\r\3\2\2")
        buf.write("\2?@\7\22\2\2@A\7\t\2\2AB\5\20\t\2BC\7\3\2\2C\17\3\2\2")
        buf.write("\2DE\b\t\1\2EL\7\23\2\2FL\7\22\2\2GH\7\5\2\2HI\5\20\t")
        buf.write("\2IJ\7\6\2\2JL\3\2\2\2KD\3\2\2\2KF\3\2\2\2KG\3\2\2\2L")
        buf.write("U\3\2\2\2MN\f\7\2\2NO\t\3\2\2OT\5\20\t\bPQ\f\6\2\2QR\t")
        buf.write("\4\2\2RT\5\20\t\7SM\3\2\2\2SP\3\2\2\2TW\3\2\2\2US\3\2")
        buf.write("\2\2UV\3\2\2\2V\21\3\2\2\2WU\3\2\2\2\t\27\35*.KSU")
        return buf.getvalue()


class MiGramaticaParser ( Parser ):

    grammarFileName = "MiGramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'for'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'>'", "'<'", "'=='", "'!='", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forStmt = 2
    RULE_inicializacion = 3
    RULE_condicion = 4
    RULE_actualizacion = 5
    RULE_asignacion = 6
    RULE_expresion = 7

    ruleNames =  [ "programa", "sentencia", "forStmt", "inicializacion", 
                   "condicion", "actualizacion", "asignacion", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    INT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiGramaticaParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = MiGramaticaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sentencia()
                self.state = 17
                self.match(MiGramaticaParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiGramaticaParser.T__1 or _la==MiGramaticaParser.ID):
                    break

            self.state = 23
            self.match(MiGramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forStmt(self):
            return self.getTypedRuleContext(MiGramaticaParser.ForStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.AsignacionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = MiGramaticaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.forStmt()
                pass
            elif token in [MiGramaticaParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.asignacion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForLoopContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ForStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def inicializacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.InicializacionContext,0)

        def condicion(self):
            return self.getTypedRuleContext(MiGramaticaParser.CondicionContext,0)

        def actualizacion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ActualizacionContext,0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.SentenciaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForLoop" ):
                return visitor.visitForLoop(self)
            else:
                return visitor.visitChildren(self)



    def forStmt(self):

        localctx = MiGramaticaParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            localctx = MiGramaticaParser.ForLoopContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(MiGramaticaParser.T__1)
            self.state = 30
            self.match(MiGramaticaParser.T__2)
            self.state = 31
            self.inicializacion()
            self.state = 32
            self.match(MiGramaticaParser.T__0)
            self.state = 33
            self.condicion()
            self.state = 34
            self.match(MiGramaticaParser.T__0)
            self.state = 35
            self.actualizacion()
            self.state = 36
            self.match(MiGramaticaParser.T__3)
            self.state = 37
            self.match(MiGramaticaParser.T__4)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiGramaticaParser.T__1 or _la==MiGramaticaParser.ID:
                self.state = 38
                self.sentencia()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiGramaticaParser.T__0:
                    self.state = 39
                    self.match(MiGramaticaParser.T__0)


                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(MiGramaticaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InicializacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_inicializacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicializacion" ):
                listener.enterInicializacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicializacion" ):
                listener.exitInicializacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicializacion" ):
                return visitor.visitInicializacion(self)
            else:
                return visitor.visitChildren(self)




    def inicializacion(self):

        localctx = MiGramaticaParser.InicializacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inicializacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MiGramaticaParser.ID)
            self.state = 50
            self.match(MiGramaticaParser.T__6)
            self.state = 51
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def getRuleIndex(self):
            return MiGramaticaParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = MiGramaticaParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MiGramaticaParser.ID)
            self.state = 54
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiGramaticaParser.T__7) | (1 << MiGramaticaParser.T__8) | (1 << MiGramaticaParser.T__9) | (1 << MiGramaticaParser.T__10))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 55
            self.match(MiGramaticaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_actualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActualizacion" ):
                listener.enterActualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActualizacion" ):
                listener.exitActualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizacion" ):
                return visitor.visitActualizacion(self)
            else:
                return visitor.visitChildren(self)




    def actualizacion(self):

        localctx = MiGramaticaParser.ActualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actualizacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(MiGramaticaParser.ID)
            self.state = 58
            self.match(MiGramaticaParser.T__6)
            self.state = 59
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)
        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def asignacion(self):

        localctx = MiGramaticaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            localctx = MiGramaticaParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MiGramaticaParser.ID)
            self.state = 62
            self.match(MiGramaticaParser.T__6)
            self.state = 63
            self.expresion(0)
            self.state = 64
            self.match(MiGramaticaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiGramaticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiGramaticaParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiGramaticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(MiGramaticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiGramaticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiGramaticaParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiGramaticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiGramaticaParser.INT]:
                localctx = MiGramaticaParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 67
                self.match(MiGramaticaParser.INT)
                pass
            elif token in [MiGramaticaParser.ID]:
                localctx = MiGramaticaParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 68
                self.match(MiGramaticaParser.ID)
                pass
            elif token in [MiGramaticaParser.T__2]:
                localctx = MiGramaticaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(MiGramaticaParser.T__2)
                self.state = 70
                self.expresion(0)
                self.state = 71
                self.match(MiGramaticaParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 81
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MiGramaticaParser.MulDivContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__11 or _la==MiGramaticaParser.T__12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = MiGramaticaParser.AddSubContext(self, MiGramaticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 78
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MiGramaticaParser.T__13 or _la==MiGramaticaParser.T__14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expresion(5)
                        pass

             
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




