# -*- coding: cp1252 -*-
# -----------------------------------------------------------------------------
# Analizador l�xico
# -----------------------------------------------------------------------------

# importa el primer m�dulo del ply
import ply.lex as lex
import re

tokens = [
   
    # Operadores aritm�ticos
    'MAS',
    'MENOS',
    'MULTI',
    'DIVISION',
    'MODULO',
    'IGUAL',

    # Operadores de comparaci�n
    'MENOR',
    'MAYOR',
    'MENORIG',
    'MAYORIG',
    'COMPARAR',
    'DIFERCOMP',
    'DIFER',
    
    # Operadores l�gicos
    'AND',
    'OR',
    
    # Literales
    'PUNTO',
    'PUNTOCOMA',
    'COMA',
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZ',
    'LLAVEDER',
    'CORCHIZ',
    'CORCHDER',

    # Tipos de datos
    'ENTNUM',
    'CIENTNUM',
    'CADENA',
    'BINARIO',
    'ID',

    # Tipos de comentarios
    'COMENTSIMP',
    'COMENTMULT',
]

reserved = {
    'class' : 'CLASS',
    'extends' : 'EXTENDS',
    'void' : 'VOID',
    'type' : 'TYPE',
    'float' : 'FLOAT',
    'int' : 'INT',
    'boolean' : 'BOOLEAN',
    'string' : 'STRING',
    'return' : 'RETURN',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'this' : 'THIS',
    'new' : 'NEW',
    'length' : 'LENGTH',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
    'return' : 'RETURN'
    
}

tokens = tokens + list(reserved.values())

t_MAS = r'\+'
t_MENOS = r'\-'
t_MULTI = r'\*'
t_DIVISION = r'/'
t_MODULO = r'%'

t_MENOR = r'<'
t_MAYOR = r'>'
t_MENORIG = r'<='
t_MAYORIG = r'>='
t_COMPARAR = r'=='
t_DIFERCOMP = r'!='
t_DIFER = r'!'
t_IGUAL = r'='

t_AND = r'and'
t_OR = r'or'

t_PUNTO = r'\.'
t_COMA = r','
t_PUNTOCOMA = r';'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZ = r'\{'
t_LLAVEDER = r'\}'
t_CORCHIZ = r'\['
t_CORCHDER = r'\]'


# Definimos funci�n para reconocer comentarios simples (una sola linea //)
def t_COMENTSIMP(t):
    r'(\/){2}(.|\d)*[\n]'
    return t

# Definimos funci�n para reconocer comentarios m�ltiples /* texto
# incluyendo saltos de lineas */
def t_COMENTMULT(t):
    r'/[*](.|\n)*?[*]/'
    return t


#Definimos una funci�n que se encargue de reconocer la e.r de numeros cientificos
def t_CIENTNUM(t):
    r'-?(0|[1-9]\d*)(\.)?\d+(E|e)-?\d+'    
    return t


# Definimos una funcion de error para los ceros a la izquierda de un numero
def t_errornument(t):
    r'-?0[0-9]'
    print "\nERROR en la linea: '%d'\n ERROR en:'%s'\nError de ceros a la izquierda en el numero\n" % (t.lexer.lineno,t.value)


# Definimos una funci�n que reconozca el error en IDes
# con final numero
def t_erroridnumfin(t):
    r'[_a-zA-Z]+([��]|[����������])*\w*(\d)+(\s)+'
    print "\nERROR en la linea: '%d'\n ERROR en:'%s'\nEl ID no puede terminar con un numero\n" % (t.lexer.lineno,t.value)

# Definimos una funci�n que reconozca el error en IDes
# con Inicio de numero
def t_erroridnumini(t):
    r'(\d)+([��]|[����������])*\w*'
    print "\nERROR en la linea: '%d'\n ERROR en:'%s'\nEl ID no puede Iniciar con un numero\n" % (t.lexer.lineno,t.value)


#Definimos una funci�n que se encargue de reconocer Numeros Binarios formato: b�100001� y pasarlos a decimal.
def t_BINARIO(t):
    r'b(\�)(0|1)*(\�)'
    cadena=t.value #Ingreso t.value en "cadena"
##    print cadena  #Debe imprimir en formato b�100001� la cadena.
    patron = re.compile ('(?P<binario>(0|1)+)') #Defino un grupo con nombre "binario"
    result = patron.search(cadena) #Busco en "cadena" la expresion definida en el paso anterior.
##    print result.group('binario') #Imprime la expesion que encontro que coincidia.
    a = int(result.group('binario'), 2) #Convierte la expresion encontrada de Binario a decimal y el decimal lo guarda en "a"
##    print type (a) #Para saber el tipo de dato <type 'str'>
##    print type (t) #Para saber el tipo de dato <class 'ply.lex.LexToken'>
    t.value = a #Le cambio el valor por el del binario.
    return t



def t_ENTNUM(t):
    r'-?\d+'                                    
    t.value = int(t.value)   # int(t.value) se encarga de transformar el texto leido en el c�digo fuente a entero
    if t.value < 2147483647 and t.value > -2147483648:
        return t
    else:
        print "Valor entero fuera de rango, debe ser de 32 bits como maximo"

# Definimos una funci�n que se encarga de reconocer los IDes
# que inician con # � Vocales tildadas.
def t_errorid(t):
        r'((\d)|[��]|[����������])+\w*'
        print "\nERROR en la linea: '%d'\n ERROR en:'%s'\nEl ID No puede iniciar ni con [#] [�-�] [vocales tildadas]\n" % (t.lexer.lineno,t.value) 



def t_FLOAT(t):
    r'[+-]?\d+(\.)(\d+([eE][+-]?\d+)?)'
    return t
    
# Definimos una funci�n que se encarga de reconocer los IDes
# que no coinciden con las palabras reservadas
def t_ID(t):       
        r'[_a-zA-Z]+([��]|[����������])*\w*'           # \w = [a-zA-Z0-9_] 
        if '�' in t.value:
            t.value=t.value.replace('�', '_')            

        t.type = reserved.get(t.value, 'ID')    # Tenemos que definir t_ID como funcion para primero evaluar si el valor de t esta dentro de las palabras reservadas,
        return t                           # ya que estas corresponden a la expresion regular de un ID. Si no esta alli, lo reconoce como ID


#Definimos una funci�n que se encargue de reconocer cadenas de texto
def t_CADENA(t):
    r'".*"'
    return t


# Definimos un componente l�xico que se encargue de ignorar los
# espacios en blanco y las tabulaciones.
t_ignore  = ' \t'

# Definimos una funcion que me reconozca el salto de linea contenido
# en el c�digo fuente
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)   # Suma el numero de saltos de
                                     # linea (\n) y los agrega al valor de t.lexer.lineno


# DEFINIMOS FUNCIONES QUE SE ENCARGUEN DE RECONOCER ERRORES ESPECIF�COS


# Definimos una funcion de error para los comentarios m�ltiples
def t_errorcomentmult(t):
    r'/[*]|[*]/'
    print "\nERROR EN:'%s'\nFalta abrir o cerrar COMENTARIO MULTIPLE\n" % (t.value)

# Definimos una funcion de error para las cadenas de texto
def t_errorcadena(t):
    r'(["]\w*)|(\w*["])'
    print "\nERROR en la linea: '%d'\n ERROR en:'%s'\nFalta abrir o cerrar la CADENA DE TEXTO\n" % (t.lexer.lineno,t.value)

# Necesitamos obligatoriamente definir una funci�n que capture los
# posibles errores que se generen durante el an�lisis l�xico
def t_error(t):
    print "Error en la linea " ,t.lexer.lineno
    t.lexer.skip(1)          #Esto me permite omitir el error y continuar con el an�lisis l�xico (no omite la linea solo el error)
                             #El argumento de skip() significa el numero de caracteres saltados despues de encontrar un error

##
##Archivo Fuente
##
analizador = lex.lex() #Crea el lexer(automata) 
##
##data=open('PruebaLexico.txt').read()  #Abre el archivo fuente.txt 
##analizador.input(data)  # Toma el archivo y se lo manda al lexer para analizarlo
##
##while 1:
##    tok = analizador.token()
##    if not tok: break      
##    print tok          #Imprime el token reconocido con:
##                       #(nombre del componente l�xico, caracteres reconocidos, linea de ubicaci�n, caracteres recorridos incluyendo saltos de linea y espacios)



