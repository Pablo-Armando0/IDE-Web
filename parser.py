def verificar_sintaxis(codigo):
    sentencias = codigo.strip().split('\n')
    resultado = []

    claves_control = ("if", "while", "for", "def", "else", "elif")

    for numero_linea, sentencia in enumerate(sentencias, 1):
        contenido = sentencia.strip()

        if contenido == "":
            resultado.append(f"Línea {numero_linea}: (vacía) ✔️")
            continue

        es_control = any(contenido.startswith(clave) for clave in claves_control)

        if es_control:
            if not contenido.endswith(":"):
                resultado.append(f"Línea {numero_linea}: ❌ falta ':' al final de una estructura de control.")
            else:
                resultado.append(f"Línea {numero_linea}: ✔️ instrucción de control válida.")
        elif "=" in contenido:
            partes = contenido.split("=")
            if len(partes) != 2:
                resultado.append(f"Línea {numero_linea}: ❌ demasiados signos '=' o asignación mal formada.")
                continue

            lado_izq, lado_der = partes
            if not lado_izq.strip().isidentifier():
                resultado.append(f"Línea {numero_linea}: ❌ lado izquierdo inválido en la asignación.")
            elif lado_der.strip() == "":
                resultado.append(f"Línea {numero_linea}: ❌ lado derecho vacío en la asignación.")
            else:
                resultado.append(f"Línea {numero_linea}: ✔️ asignación válida.")
        else:
            resultado.append(f"Línea {numero_linea}: ❌ instrucción no reconocida o incompleta.")

    return '\n'.join(resultado)