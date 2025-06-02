def simular_turing(cadena): 
    cinta = list(cadena.strip()) + ['_']  
    indice = 0
    estado = 'q0'
    historial = []


    transiciones = {
        ('q0', 'a'): ('q0', 'X', 'R'),
        ('q0', 'b'): ('q0', 'Y', 'R'),
        ('q0', '_'): ('qf', '_', 'N')  
    }

    while estado != 'qf':
        simbolo = cinta[indice]
        clave = (estado, simbolo)

        if clave in transiciones:
            nuevo_estado, nuevo_simbolo, direccion = transiciones[clave]
            historial.append(f"Estado {estado} | Posición {indice} | '{simbolo}' → '{nuevo_simbolo}' | {direccion} → {nuevo_estado}")
            cinta[indice] = nuevo_simbolo
            estado = nuevo_estado

            if direccion == 'R':
                indice += 1
                if indice >= len(cinta):
                    cinta.append('_')  
            elif direccion == 'L':
                indice -= 1
                if indice < 0:
                    cinta.insert(0, '_')
                    indice = 0
        else:
            historial.append(f"ERROR: No hay transición definida para (estado={estado}, símbolo='{simbolo}')")
            break


    ultima_letra = None
    for i in range(len(cinta)-2, -1, -1):
        if cinta[i] in ['X', 'Y']:  
            ultima_letra = 'a' if cinta[i] == 'X' else 'b'
            break

    if ultima_letra == 'a':
        resultado_final = " Resultado: HUMANO"
    elif ultima_letra == 'b':
        resultado_final = " Resultado: ROBOT"
    else:
        resultado_final = " No se pudo determinar si es humano o robot."

    resultado = ''.join(cinta).rstrip('_')
    historial.append(f"Resultado final en la cinta: {resultado}")
    historial.append(resultado_final)
    return '\n'.join(historial) 