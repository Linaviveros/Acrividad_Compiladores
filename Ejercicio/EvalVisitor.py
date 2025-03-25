from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitAsignacion(self, ctx: MiGramaticaParser.AsignacionContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        if value is None:
            value = 0  
        self.variables[var_name] = value
        print(f" Asignación: {var_name} = {value}")

    def visitExpresion(self, ctx: MiGramaticaParser.ExpresionContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, 0)
        elif ctx.getChildCount() == 3:
            left = self.visit(ctx.expresion(0))
            right = self.visit(ctx.expresion(1))
            op = ctx.getChild(1).getText()
            if left is None: left = 0  
            if right is None: right = 0  
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left // right if right != 0 else 0
        return 0

    def visitForLoop(self, ctx: MiGramaticaParser.ForLoopContext):
        self.visit(ctx.inicializacion())  

        while self.visit(ctx.condicion()):  
            for sentencia in ctx.sentencia():  
                self.visit(sentencia)
            self.visit(ctx.actualizacion())  
            print(f" Fin de iteración, variables: {self.variables}")  #  Debug para verificar valores de `i`

    def visitInicializacion(self, ctx: MiGramaticaParser.InicializacionContext):
        return self.visit(ctx.getChild(0))  

    def visitCondicion(self, ctx: MiGramaticaParser.CondicionContext):
        var_name = ctx.ID().getText()
        left = self.variables.get(var_name, 0)  #  Leer `i` correctamente
        right = int(ctx.INT().getText())
        op = ctx.op.text

        print(f" Evaluando condición: {left} {op} {right}")  

        if op == '<': return left < right
        if op == '>': return left > right
        if op == '<=': return left <= right
        if op == '>=': return left >= right
        if op == '==': return left == right
        return False

    def visitActualizacion(self, ctx: MiGramaticaParser.ActualizacionContext):
        var_name = ctx.ID().getText()
        old_value = self.variables.get(var_name, 0)  #  Obtener el valor actual de `i`
        new_value = self.visit(ctx.expresion())

        if new_value is None:
            new_value = old_value + 1  #  Si algo falla, sumamos manualmente

        self.variables[var_name] = new_value  #  Ahora sí, `i` se actualiza bien
        print(f" Actualización correcta: {var_name} = {new_value}")  
