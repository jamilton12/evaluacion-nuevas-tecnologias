# Proyecto de Gestión de Estudiantes en Excel

Este proyecto crea un archivo Excel con los nombres de estudiantes y sus respectivas calificaciones. Los estudiantes son ingresados por el usuario a través de la consola, y el programa determina si la calificación es "Buena" (si es 70 o mayor) o "Regular" (si es menor a 70). El archivo Excel resultante se guarda en formato `.xlsx`.

## Requisitos

- Python 3.x
- Librería `openpyxl`

## Instalación

### 1. Clonar el repositorio

Para clonar el repositorio en tu máquina local, utiliza el siguiente comando en la terminal:

```bash
git clone https://github.com/jamilton12/evaluacion-nuevas-tecnologias.git
```
### 2. Crear un entorno virtual

Es una buena práctica usar entornos virtuales para gestionar las dependencias de tu proyecto. Aquí están los pasos para crear y activar un entorno virtual:

1. **Crea un entorno virtual**:

   ```bash
   python -m venv .venv
   ```

2. **Activa el entorno virtual**:

   - En **Windows**:
   
     ```bash
     .venv\Scripts\activate
     ```

   - En **Mac/Linux**:

     ```bash
     source venv/bin/activate
     ```

3. **Instala las dependencias del proyecto**:

   Con el entorno virtual activado, instala la librería `openpyxl` usando `pip`:

   ```bash
   pip install openpyxl
   ```

## Uso

1. Clona o descarga el proyecto en tu máquina local.
2. Abre una terminal o consola.
3. Navega al directorio del proyecto:

   ```bash
   cd evaluacion-nuevas-tecnologias
   ```

4. Si no has creado aún un entorno virtual, sigue los pasos de instalación anteriores.
5. Ejecuta el script Python:

   ```bash
   python main.py
   ```

6. Ingresa los nombres y notas de 3 estudiantes cuando se te solicite.

El programa creará un archivo llamado `ejercicio3.xlsx` en el mismo directorio donde se ejecutó el script. El archivo Excel tendrá el siguiente formato:

| Estudiante | Clasificación |
|------------|---------------|
| Nombre 1   | Bueno/Regular |
| Nombre 2   | Bueno/Regular |
| Nombre 3   | Bueno/Regular |

## Descripción del código

1. **Entrada de datos**: El programa solicita el nombre y la calificación de 3 estudiantes. Cada par de datos se almacena en un diccionario y se agrega a una lista.
   
2. **Creación del archivo Excel**: Utilizando la librería `openpyxl`, el programa crea un archivo Excel con los encabezados "Estudiante" y "Clasificación".
   
3. **Clasificación**: En función de la calificación, se asigna la clasificación "Bueno" si la nota es 70 o superior, y "Regular" si es inferior a 70.
   
4. **Guardado del archivo**: El archivo Excel se guarda con el nombre `ejercicio3.xlsx`.

## Contribuciones

Si deseas realizar mejoras o agregar nuevas funcionalidades, no dudes en hacer un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto es de código abierto y se distribuye bajo la [Licencia MIT](https://opensource.org/licenses/MIT).
