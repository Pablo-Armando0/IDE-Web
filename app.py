from flask import Flask, request, jsonify, render_template
from lexer import escanear_lexico
from parser import verificar_sintaxis
from turing import simular_turing
import os

servidor = Flask(__name__)

# Página principal
@servidor.route('/')
def cargar_interfaz():
    return render_template('IDE.html')

# análisis léxico
@servidor.route('/lexico', methods=['POST'])
def procesar_lexico():
    contenido = request.get_json()
    codigo = contenido.get('code', '')
    try:
        salida = escanear_lexico(codigo)
        return jsonify({
            'resultado': salida,
            'error': False
        })
    except Exception as e:
        return jsonify({
            'resultado': str(e),
            'error': True,
            'linea': getattr(e, 'linea', 1)
        })

# análisis sintáctico
@servidor.route('/sintaxis', methods=['POST'])
def procesar_sintaxis():
    contenido = request.get_json()
    codigo = contenido.get('code', '')
    try:
        salida = verificar_sintaxis(codigo)
        return jsonify({
            'resultado': salida,
            'error': False
        })
    except Exception as e:
        return jsonify({
            'resultado': str(e),
            'error': True,
            'linea': getattr(e, 'linea', 1)
        })

# máquina de Turing
@servidor.route('/maquina-turing', methods=['POST'])
def procesar_turing():
    contenido = request.get_json()
    codigo = contenido.get('code', '')
    try:
        salida = simular_turing(codigo)
        return jsonify({
            'resultado': salida,
            'error': False
        })
    except Exception as e:
        return jsonify({
            'resultado': str(e),
            'error': True,
            'linea': getattr(e, 'linea', 1)
        })

# Ejecutar servidor
if __name__ == '__main__':
    servidor.run(debug=True)