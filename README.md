## IDE WEB

## Analiszador Léxico, Sintáctico y Máquina de Turing 
 
 ## Información del Estudiante
- **Nombre del Estudiante**: [Arias Hernandez Pablo Armando]
- **Materia**: [Lenguaje y Automatas I]
- **Profesor**: [Kevin David Molina Gomez]
- **carrera**: [Ingeneria en Sistemas Computacionales]
- **Fecha**: [1 de junio del 2025]

## resumen del proyecto
Este poryecto implementa dos analizadores y un Método:
1.- analizador Léxico
2.- analizador Sintáctico
3.- una Máquina de Turing que ayuda a detectar humano o robot

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

### El analizador sintáctico

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

### Descripción 
La implementación de la máquina de Turing determina si una cadena proviene de un humano o un robot al evaluar su último carácter.

#### Características Principales:
1. *Estados*:
   - Estado inicial: q0
   - Estado final: qf

2. *Alfabeto de entrada*:
   - a: representa características de humano
   - b: representa características de robot
   - _: representa el fin de la cadena

3. *Transiciones*:
   - (q0, a) → (q0, X, R): Reemplaza 'a' por 'X' y mueve a la derecha
   - (q0, b) → (q0, Y, R): Reemplaza 'b' por 'Y' y mueve a la derecha
   - (q0, _) → (qf, _, N): Al encontrar espacio en blanco, termina

#### Funcionamiento:
1. La máquina lee la cadena de izquierda a derecha
2. Reemplaza cada 'a' por 'X' y cada 'b' por 'Y'
3. La última letra procesada determina el resultado:
   - Si la última letra es 'X' (originalmente 'a'): HUMANO
   - Si la última letra es 'Y' (originalmente 'b'): ROBOT


#### Ejemplos de Uso:

*Entradas Válidas*:
```
aaa -> HUMANO
bbb -> ROBOT
aba -> HUMANO
bab -> ROBOT
```

*Entradas No Válidas*:
```
- Cadenas vacías
- Caracteres diferentes a 'a' o 'b'
- Espacios en medio de la cadena
```
#### Resultados Posibles:
1. "Resultado: HUMANO" - cuando la última letra procesada es 'a'
2. "Resultado: ROBOT" - cuando la última letra procesada es 'b'
3. "No se pudo determinar si es humano o robot" - cuando hay un error o la cadena está vacía

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
  
## Estructura del Proyecto

```
proyecto/
│
├── app.py          # Servidor web Flask
├── lexer.py        # Analizador léxico
├── parser.py       # Analizador sintáctico
├── turing.py       # Máquina de Turing
│
├── templates/      # Plantillas HTML
│   └── index.html
│
└── static/         # Archivos estáticos
    ├── css/
    ├── img/
    └── js/
```

Esta estructura organiza el proyecto de la siguiente manera:

- *app.py*: Contiene la configuración y rutas del servidor web Flask
- *lexer.py*: Implementa el analizador léxico para el procesamiento de tokens
- *parser.py*: Implementa el analizador sintáctico para validar la estructura
- *turing.py*: Contiene la implementación de la máquina de Turing
- *templates/*: Directorio con las plantillas HTML para la interfaz web
- *static/*: Directorio para archivos estáticos como CSS, imágenes y JavaScript

 ## evidandica visual

incio de la paguina
[![photo-5035172470033854011-y.jpg](https://i.postimg.cc/mDZD7MMV/photo-5035172470033854011-y.jpg)](https://postimg.cc/zLM8ryxR)

ejecucion del lexico
[![photo-5035172470033854007-y.jpg](https://i.postimg.cc/85gdGZ2c/photo-5035172470033854007-y.jpg)](https://postimg.cc/5HpQqSNW)

ejecucion del sintactico 
[![photo-5035172470033854008-y.jpg](https://i.postimg.cc/fyyYfy1n/photo-5035172470033854008-y.jpg)](https://postimg.cc/ctqKsxsX)

ejecucion de la maquina de turing
deteccion por humano
[![photo-5035172470033854010-y.jpg](https://i.postimg.cc/52G6djh2/photo-5035172470033854010-y.jpg)](https://postimg.cc/FYy90FFM)


con robot
[![photo-5035172470033854012-y.jpg](https://i.postimg.cc/rmd66wLM/photo-5035172470033854012-y.jpg)](https://postimg.cc/tZHvWyTM)

no detectable
[![photo-5035172470033854009-y.jpg](https://i.postimg.cc/pd2Krm0Y/photo-5035172470033854009-y.jpg)](https://postimg.cc/VJVJHkPd)
