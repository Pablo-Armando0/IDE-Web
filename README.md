## Información del Estudiante
- **Nombre del Estudiante**: [Arias Hernandez Pablo Armando]
- **Materia**: [Lenguaje y Automatas I]
- **Profesor**: [Kevin David Molina Gomez]
- **carrera**: [Ingeneria en Sistemas Computacionales]
- **Fecha**: [1 de junio del 2025]

## Instrucciones para Ejecutar el Proyecto

### Requisitos Previos
- Python 3.x instalado en el sistema
- Flask
- Navegador web moderno (Chrome, Firefox, Edge)
- Conexión a Internet (para las dependencias CDN)

### Instalación
1. Instalar las dependencias:
```bash
pip install flask
```

2. **Ejecutar el Servidor**
   ```bash
   python app.py
   ```

4. **Acceder al IDE**
   - abrir el codigo app.py y dar a ejecutar para que de la ip del servidor del servidor
   - El IDE web se cargará automáticamente

## Explicación del Lenguaje Personalizado

### Tokens y Análisis Léxico
El analizador léxico reconoce los siguientes elementos:

1. **Palabras Clave** (`[CLAVE]`):
   - if
   - else
   - while
   - for
   - return

2. **Símbolos y Operadores** (`[simbolo]`):
   - Operadores aritméticos: `+`, `-`, `*`, `/`
   - Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
   - Delimitadores: `(`, `)`, `{`, `}`, `;`

3. **Números** (`[numero]`):
   - Cualquier secuencia de dígitos

4. **Identificadores** (`[letra]`):
   - Nombres de variables y funciones
   - Deben comenzar con una letra

### Gramática

El analizador sintáctico verifica:

1. **Estructuras de Control**:
   - Deben terminar con dos puntos (:)
   - Ejemplos: if, while, for, def

2. **Asignaciones**:
   - Formato: variable = valor
   - El lado izquierdo debe ser un identificador válido
   - El lado derecho no puede estar vacío

### Manejo de Errores

El sistema detecta los siguientes errores:
1. Falta de dos puntos (:) en estructuras de control
2. Asignaciones mal formadas
3. Identificadores inválidos
4. Instrucciones no reconocidas o incompletas

## Ejemplos

### Entradas Válidas
```
x = 2
contador = 42
resultado = 100
y = 1
```

### Entradas Inválidas
```
x =           # Error: lado derecho vacío
1x = 42       # Error: identificador inválido
xyz          # Error: no es una asignación
= 100         # Error: falta identificador
```

## Máquina de Turing

### Características del IDE Web
- Editor con números de línea
- Resaltado de errores en tiempo real
- Análisis léxico y sintáctico interactivo
- Interfaz moderna y responsive
- Feedback inmediato de errores

### Funcionalidades Implementadas
El proyecto incluye una interfaz web (IDE.html) que permite:
- ✅ Análisis Léxico: Identifica tokens y elementos del lenguaje
- ✅ Análisis Sintáctico: Valida la estructura de las asignaciones
- ✅ Resaltado de Errores: Subraya las líneas con problemas
- ✅ Máquina de Turing: Procesamiento de cadenas
- ✅ Visualizar los resultados de cada análisis
 
 ## evidandica visual

incio de la paguina
inicio.jpg

ejecucion del lexico
lexico.png

ejecucion del sintactico 
sintactico.jpg

ejecucion de la maquina de turing
deteccion por humano
turing.jpg


con robot
turing2.jpg

no detectable
turing3.jpg
