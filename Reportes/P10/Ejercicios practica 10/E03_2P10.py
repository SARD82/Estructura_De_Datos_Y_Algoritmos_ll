a3 = open(r'C:\Users\santi\OneDrive\Documentos\Santiago\Programación\FI\EDA 2\Reportes\P10\Ejercicios practica 10\Ejercicio1.txt', 'r') # cambiar ruta

print("Segundo metodo: ")
while True:
    linea = a3.readline()
    if not linea:
        break
    print(linea.strip())

a3.close()