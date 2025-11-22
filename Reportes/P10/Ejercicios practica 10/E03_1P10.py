archivo = open(r'C:\Users\santi\OneDrive\Documentos\Santiago\Programación\FI\EDA 2\Reportes\P10\Ejercicios practica 10\Ejercicio1.txt', 'r') # Cambiar ruta

c1 = archivo.read(3)
c2 = archivo.read()

print("Primer código:")
print("Primeros 3 byts o primeros 3 caracteres: \n", c1)
print("Resto del archivo: \n", c2)

archivo.close()