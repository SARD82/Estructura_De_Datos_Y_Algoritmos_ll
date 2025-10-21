class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = []

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].agregarVecino(v)
            self.vertices[v].agregarVecino(u)
            return True
        return False

    def imprimeGrafo(self):
        for key in sorted(self.vertices.keys()):
            print("Vértice", key, "-> Sus vecinos son: ", self.vertices[key].vecinos)

class Controladora:
    def main(self):
        g = Grafo()
        for i in range(ord('A'), ord('Q')):  
            g.agregaVertice(Vertice(chr(i)))
 
        edges  =  []
 
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        g.imprimeGrafo()

obj = Controladora()
obj.main() 