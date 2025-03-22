import openpyxl as op

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario
# --- Escribe tu código aquí ---

estudiantes = list()

for i in range(3):
    nombre =  input('Ingrese el nombre de un estudiante \n')
    nota = float(input('Ingrese la nota del estudiante \n'))
    estudiantes.append({ 'nombre': nombre, 'nota': nota })


# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = op.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezados
# Escribe "Estudiante" en A1 y "Clasificación" en B1
# --- Escribe tu código aquí ---

hoja['A1'] = 'Estudaintes'
hoja['B1'] = 'Calificaciones'

# PARTE 4: Escribir datos con ciclo y condicional
fila = 2
# Usa un ciclo for para recorrer el diccionario
# Escribe el nombre en A y "Bueno" o "Regular" en B según si la nota > 70
# Incrementa 'fila' en cada iteración
# --- Escribe tu código aquí ---

for estudiante in estudiantes:
    hoja[f'A{fila}'] = estudiante['nombre'] 
    if estudiante['nota'] >= 70:
        hoja[f'B{fila}'] = "Bueno"
    else :
        hoja[f'B{fila}'] = 'Regular'
    fila += 1
# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio2.xlsx"
# --- Escribe tu código aquí ---

libro.save('ejerciocio3.xlsx')

print("¡Ejercicio 3 guardado en ejercicio3.xlsx!")