class Vertice:
    def __init__(self, n):
        self.nombre=n
        self.vecinos= list()
        self.distancia = 0
        self.color = 'white'
        self.pred = -1
        
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)
            self.vecinos.sort()
            
class Grafo:
    vertices={}
    
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre]=vertice
            return True
        else:
            return False
        
    def agregarArista(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.agregarVecino(v)
                if key == v:
                    value.agregarVecino(u)
            return True
        else:
            return False
        
    def bfs(self, vert):
        vert.distancia = 0
        vert.color = 'gris'
        vert.pred = -1
        q = list()
        
        q.append(vert.nombre)
        
        while len(q) > 0:
            #MODIFICACIÒN
            u = q.pop(0)
            # u = q.pop()
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v = self.vertices[v]
                if node_v.color == 'white':
                    node_v.color = 'gris'
                    node_v.distancia = node_u.distancia + 1
                    node_v.pred = node_u.nombre
                    q.append(v)
                self.vertices[u].color = 'black'
                
    def imprimeGrafo(self):
        print(" - Grafo 1 - ")
        for key in sorted(list(self.vertices.keys())):
            print("vertice "+key+" sus vecinos son "+str(self.vertices[key].vecinos))
            print("Vertice "+key+ "El predecesor es "+str(self.vertices[key].pred))
            print("La distancia de A a "+key+" es: "+str(self.vertices[key].distancia))

class Controladora:
    def main(self):
        #Se crea un objeto 'g' de la clase Grafo, el grafo
        g=Grafo()
        #Se crea un objeto 'a' de la clase Vertice, un vertice
        a=Vertice('A')
        #Se agrega el vertice al grafo
        g.agregarVertice(a)
        
        #Esta estructura de repeticiòn es para agregar
        #todos los vertices y no hacerlo uno a uno
        for i in range (ord('A'), ord('K')):
            g.agregarVertice(Vertice(chr(i)))
            
        #Se declara una lista que contiene las aristas del grafo
        edges=['AB','AC','AD', 'DH', 'CB', 'DC', 'BE', 'BF', 'CG', 'CH', 'CE', 'EG', 'FG', 'FJ', 'GH', 'GJ', 'HI', 'JI' ]
        
        #Se agregan las aristas al grafo
        for edge in edges:
            g.agregarArista(edge[:1],edge[1:])
            #Se imprime el grafo, como lista de adyacencia
            
        for i in range(ord('A'), ord('K')):
            g.bfs(Vertice(chr(i)))
            
        g.imprimeGrafo()
        
obj=Controladora()
obj.main()