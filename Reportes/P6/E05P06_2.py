class Vertice:
    def __init__(self, n):
        self.nombre = n
        self.vecinos = []
        self.distancia = 0
        self.color = 'white'
        self.pred = -1

    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()


class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre] = vertice
            return True
        else:
            return False

    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].agregarVecino(v)
            self.vertices[v].agregarVecino(u)
            return True
        else:
            return False

    def bfs(self, inicio_nombre):
        for v in self.vertices.values():
            v.color = 'white'
            v.distancia = 0
            v.pred = -1

        inicio = self.vertices[inicio_nombre]
        inicio.color = 'gris'
        inicio.distancia = 0
        inicio.pred = -1

        q = [inicio.nombre]

        while q:
            u = q.pop(0)
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gris'
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    q.append(v)
            node_u.color = 'black'

    def imprimeGrafo(self):
        print("- GRAFO 1 -")
        for key in sorted(self.vertices.keys()):
            v = self.vertices[key]
            print(f"Vértice {key}, vecinos: {v.vecinos}, Su predecesor es: {v.pred}, La distancia es: {v.distancia}")


class Controladora:
    def main(self):
        g = Grafo()

        for i in range(ord('A'), ord('Q')):  
            g.agregarVertice(Vertice(chr(i)))

        edges = []

        for edge in edges:
            g.agregarArista(edge[0], edge[1])

        g.bfs('A')
        g.imprimeGrafo()

c = Controladora()
c.main()