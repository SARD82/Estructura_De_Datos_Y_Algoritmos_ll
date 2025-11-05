class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.val = valor

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def obtenerRaiz(self):
        return self.raiz
    
    def agregar(self, val):
        if self.raiz is None:
            self.raiz = Nodo(val)
        else:
            self.agregarNodo(val, self.raiz)

    def agregarNodo(self, val, nodo):
        if val < nodo.val:
            if nodo.hijoIzq is not None:
                self.agregarNodo(val, nodo.hijoIzq)
            else:
                nodo.hijoIzq = Nodo(val)
        else:
            if nodo.hijoDer is not None:
                self.agregarNodo(val, nodo.hijoDer)
            else:
                nodo.hijoDer = Nodo(val)
    
    def preOrden(self, nodo):
        if (nodo != None):
            print(str(nodo.val))
            if nodo.hijoIzq != None:
                self.preOrden(nodo.hijoIzq)
            if nodo.hijoDer != None:
                self.preOrden(nodo.hijoDer)
    
    def imprimePreorden(self):
        if self.raiz != None:
            self.preOrden(self.raiz)

class Controladora:
    def main(self):
        nodos = [5, 4, 6, 3, 7, 8]
        arbol = Arbol()

        for i in nodos:
            arbol.agregar(i)

        arbol.imprimePreorden()

obj = Controladora()
obj.main()