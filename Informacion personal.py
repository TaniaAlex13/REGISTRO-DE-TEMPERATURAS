#Crea un diccionario
informacion_personal = {
    "nombre": "Tania Toapanta",
    "edad": 25,
    "ciudad": "Latacunga",
    "profesion": "Ayudante Comunicaciones"
}

print("Diccionario Inicial:", informacion_personal)

#Acceder y modificar valores
# Cambiar la ciudad
informacion_personal["ciudad"] = "Quito"

# Agregar (o modificar) la profesión
informacion_personal["profesion"] = "Militar"

#Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

#Eliminar una Clave
informacion_personal.pop("edad")

#Imprimir el Diccionario Final
print("Diccionario final:", informacion_personal)