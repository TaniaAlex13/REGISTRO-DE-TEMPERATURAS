#TRABAJO DE ARCHIVOS DE TEXTO EN PYTHON
# Abrimos el archivo en modo escritura
file = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write()

file.write("Primera nota: En programacion estamos aprendiendo a crear archivos de texto en Python.\n")
file.write("Segunda nota: El practicar con ejemplos nos esta sirviendo de mucho.\n")
file.write("Tercera nota: Gracias a eso aprenderemos mas sobre el tema y lograremos presentar bien la tarea.\n")

# Cerramos el archivo después de escribir
file.close()

# Lectura del archivo de texto

# Abrimos el archivo en modo lectura
file = open("my_notes.txt", "r")

# Leemos cada línea con readline()
linea = file.readline()
while linea:
    print(linea.strip())
    linea = file.readline()

# Cerramos el archivo después de leer
file.close()
