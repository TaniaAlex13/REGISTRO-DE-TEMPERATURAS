#TRABAJO DE ARCHIVOS DE TEXTO EN PYTHON
# Abrimos el archivo en modo escritura
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando write()

archivo.write("Primera nota: En programacion estamos aprendiendo a crear archivos de texto en Python.\n")
archivo.write("Segunda nota: El practicar con ejemplos nos esta sirviendo de mucho.\n")
archivo.write("Tercera nota: Gracias a eso aprenderemos mas sobre el tema y lograremos presentar bien la tarea.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura del archivo de texto

# Abrimos el archivo en modo lectura
archivo = open("my_notes.txt", "r")

# Leemos cada línea con readline()
linea = archivo.readline()
while linea:
    print(linea.strip())
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
