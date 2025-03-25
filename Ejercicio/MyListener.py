from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print("Detectado un ciclo for.")

    def exitInicializacion(self, ctx):
        print(f"Inicialización detectada: {ctx.getText()}")

    def exitCondicion(self, ctx):
        print(f"Condición detectada: {ctx.getText()}")

    def exitActualizacion(self, ctx):
        print(f"Actualización detectada: {ctx.getText()}")

    def exitAssign(self, ctx):
        print(f"Asignación detectada: {ctx.getText()}")
