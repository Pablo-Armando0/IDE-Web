import re

def escanear_lexico(texto):
    claves = {"if", "else", "while", "for", "return"}
    operadores = {"(", ")", "{", "}", ";", "+", "-","_","-",";","-" ,"*", "/", "=", "<", ">", "==", "!=", "<=", ">="}
    
    
    patron = r'\b\w+\b|==|!=|<=|>=|[^\s\w]'


    fragmentos = re.findall(patron, texto)

    resultado_tokens = []

    for fragmento in fragmentos:
        if fragmento in claves:
            resultado_tokens.append(f"[CLAVE] → {fragmento}")
        elif fragmento in operadores:
            resultado_tokens.append(f"[simbolo] → {fragmento}")
        elif fragmento.isdigit():
            resultado_tokens.append(f"[numero] → {fragmento}")
        elif fragmento.isidentifier():
            resultado_tokens.append(f"[letra] → {fragmento}")
        else:
            resultado_tokens.append(f"[desconocido] → {fragmento}")

    return '\n'.join(resultado_tokens)
