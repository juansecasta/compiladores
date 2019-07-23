import ply.yacc as yacc
from Lexico import *
from AST import*


precedence = (
    ('left', 'MULTI', 'DIVISION', 'MODULO'),    
    ('left', 'MAS', 'MENOS'),
    ('left', 'COMPARAR', 'DIFERCOMP'),
    ('left', 'MENOR', 'MAYORIG', 'MAYOR', 'MENORIG'),
    ('left', 'AND'),
    ('left', 'OR'),    
)

# program ::= classDecl*  ***************************************************************************************************** #
def p_Programa(p):
    '''Programa : ProgramaDecl'''
    p[0]=Programa(p[1])

def p_ProgramaDecl(p):
    '''ProgramaDecl : classDecl ProgramaDecl'''
    p[0]=ProgramaDecl(p[1], p[2])
    
def p_ProgramaDecl1(p):
    '''ProgramaDecl : vacio'''
    p[0] = DeclListNull()


#classDecl ::= class id [extends id] '{' (fieldDecl | methDecl)* '}'***********************************************************#
def p_Declaracion_Clase(p):
    '''classDecl : CLASS ID ExtendsOp LLAVEIZ DeclaracionAtributos LLAVEDER''' 
    p[0]=Declaracion_Clase(p[2],p[3],p[5])

def p_ExtendsOp(p):
    '''ExtendsOp : EXTENDS ID'''
    p[0]=ExtendsOp(p[2])

def p_ExtendsOp1(p):
    '''ExtendsOp : vacio'''
    p[0] = DeclListNull()

def p_DeclaracionAtributos(p):
    '''DeclaracionAtributos : fieldmethDecl DeclaracionAtributos'''
    p[0]=Declaracion_Atributos_P(p[1], p[2])

def p_DeclaracionAtributos1(p):
    '''DeclaracionAtributos : vacio'''
    p[0] = DeclListNull()


#fieldDecl ::= type id ( ',' id )* ';'  ***************************************************************************************#
def p_fieldmethDecl(p):
    '''fieldmethDecl : Type ID ListComaID PUNTOCOMA'''
    p[0]=Declaracion_Atributos(p[1], p[2], p[3])

def p_ListComaID(p):
    '''ListComaID : COMA ID ListComaID'''
    p[0]=Declaracion_Campo_P(p[2], p[3])

def p_ListComaID1(p):
    '''ListComaID : vacio'''
    p[0] = DeclListNull()

#methDecl ::= (type | void) id '(' [formals] ')' block  *************************************************************************#
def p_fieldmethDecl1(p):
    '''fieldmethDecl :  Type ID PARENIZQ formals PARENDER block'''
    p[0]=Declaracion_Atributos_P3(p[1], p[2], p[4], p[6])

def p_fieldmethDecl2(p):
    '''fieldmethDecl :  VOID ID PARENIZQ formals PARENDER block'''
    p[0]=Declaracion_Atributos_P4(p[2], p[4], p[6])

def p_formals(p):
    '''formals : Type ID ListComaTypeID'''
    p[0]=Formales_P(p[1], p[2], p[3])


def p_formals1(p):
    '''formals : vacio'''
    p[0] = DeclListNull()

def p_ListComaTypeID(p):
    '''ListComaTypeID : COMA Type ID ListComaTypeID'''
    p[0]=Formales_P3(p[2], p[3], p[4])

def p_ListComaTypeID1(p):
    '''ListComaTypeID : vacio'''
    p[0] = DeclListNull()

#type ::= int | boolean | string | id | type '[' ']' ******************************************************************************#
def p_Type(p):
    '''Type : INT
            | BOOLEAN
            | STRING
            | Type CORCHIZ CORCHDER '''
    p[0] = Type(p[1])


def p_block(p):
    '''block : LLAVEIZ lsVarDecl lstmtDecl LLAVEDER'''
    p[0] = Bloque1(p[2], p[3])

def p_lsVarDecl(p):
    '''lsVarDecl : Declaracion_Variable lsVarDecl'''
    p[0] = Bloque2(p[1], p[2])

def p_lsVarDecl1(p):
    '''lsVarDecl : vacio'''
    p[0] = DeclListNull()

#varDecl ::= type id ['=' expr] ( ',' id ['=' expr] )* ';' ******************************************************************#
def p_Declaracion_Variable(p):
    '''Declaracion_Variable : Type ID IgualExp IdAsignExp PUNTOCOMA'''
    p[0] = Declaracion_Variable(p[1],p[2],p[3],p[4])
def p_IgualExp(p):
	'''IgualExp : IGUAL Expresion'''
	p[0] = IgualExp(p[2])
def p_IgualExp1(p):
	''' IgualExp : vacio'''
	p[0] = DeclListNull()

def p_IdAsignExp(p):
    '''IdAsignExp : COMA ID IgualExp IdAsignExp'''
    p[0] = Asignar_Valor3(p[2], p[3], p[4])

def p_IdAsignExp1(p):
    '''IdAsignExp : vacio'''
    p[0] = DeclListNull()
    

def p_lstmtDecl(p):
    '''lstmtDecl : stmt lstmtDecl'''
    p[0] = Bloque4(p[1], p[2])

def p_lstmtDecl1(p):
    '''lstmtDecl : vacio'''
    p[0] = DeclListNull()

#stmt ::= assign ';' ************************************************************************************************************#
#| call ';'
#| return [expr] ';'
#| if '(' expr ')' stmt [else stmt]
#| while '(' expr ')' stmt
#| break ';' | continue ';'
#| block  ***********************************************************************************************************************#  
def p_stmt(p):
    '''stmt : assign PUNTOCOMA'''
    p[0]=stmt(p[1])

def p_stmt2(p):
    '''stmt : call PUNTOCOMA'''
    p[0]=stmt2(p[1])

def p_stmt3(p):
    '''stmt :  RETURN Expresion PUNTOCOMA'''
    p[0]=stmt3(p[2])

def p_stmt4(p):
    '''stmt :  RETURN PUNTOCOMA'''
    p[0]=stmt4()

def p_stmt5(p):
    '''stmt : IF PARENIZQ Expresion PARENDER stmt ELSE stmt'''
    p[0]=stmt5(p[3], p[5], p[7])

def p_stmt6(p):
    '''stmt : IF PARENIZQ Expresion PARENDER stmt'''
    p[0]=stmt6(p[3], p[5])

def p_stmt7(p):
    '''stmt : WHILE PARENIZQ Expresion PARENDER stmt'''
    p[0]=stmt7(p[3], p[5])

def p_stmt8(p):
    '''stmt : BREAK PUNTOCOMA
            | CONTINUE PUNTOCOMA'''
    p[0]=stmt8(p[1])

def p_stmt9(p):
    '''stmt : block'''
    p[0]=stmt9(p[1])

#assign ::= location '=' expr   ************************************************************************************************#
def p_Asignacion(p):
    '''assign : location IGUAL Expresion'''
    p[0]=Asignacion(p[1], p[3])
def p_Asignacion1(p):
    '''assign : vacio'''
    p[0] = DeclListNull()   

#location ::= id | expr '.' id | expr '[' expr ']' *****************************************************************************#    

def p_location(p):
    '''location : ID'''
    p[0]=location1(p[1])

def p_location1(p):
    '''location : Expresion PUNTO ID'''
    p[0]=location2(p[1], p[3])

def p_location2(p):
    '''location : Expresion CORCHIZ Expresion CORCHIZ'''
    p[0]=location3(p[1], p[3])

#call ::= method '(' [actuals] ')' *********************************************************************************************#
def p_call(p):
    '''call : method PARENIZQ actuals PARENDER'''
    p[0]=Llamado(p[1], p[3])

def p_call1(p):
    '''call : method PARENIZQ PARENDER'''
    p[0]=Llamado1(p[1])
  
#method ::= id | expr '.' id ***************************************************************************************************#
def p_method(p):
    '''method : ID'''
    p[0]=Metodo(p[1])

def p_method1(p):
    '''method : Expresion PUNTO ID'''
    p[0]=Metodo_P(p[1], p[3])

#actuals ::= expr (',' expr)* **************************************************************************************************#
def p_Actuales(p):
    '''actuals : Expresion LsActualesExp'''
    p[0]=Actuales(p[1], p[2])
def p_Actuales1(p):
    '''actuals : vacio'''
    p[0] = DeclListNull()

def p_LsActualesExp(p):
    '''LsActualesExp : COMA Expresion LsActualesExp'''
    p[0]=Actuales(p[2], p[3])

def p_LsActualesExp1(p):
    '''LsActualesExp : vacio'''
    p[0] = DeclListNull()

#expr ::= location
#| call
#| this
#| new id '(' ')'
#| new type '[' expr ']'
#| expr '.' length
#| expr binary expr
#| unary expr
#| literal
#| '(' expr ')'
def p_Expresion1(p):
    '''Expresion : location'''
    p[0]= Expresion1(p[1])



def p_Expresion2(p):
    '''Expresion : call'''
    p[0]=Expresion2(p[1])

def p_Expresion3(p):
    '''Expresion : THIS'''
    p[0]=Expresion3(p[1])

def p_Expresion4(p):
    '''Expresion : NEW ID PARENIZQ PARENDER'''
    p[0]=Expresion4(p[1], p[2])

def p_Expresion5(p):
    '''Expresion : NEW Type CORCHIZ Expresion CORCHDER'''
    p[0]=Expresion5(p[2], p[4])

def p_Expresion6(p):
    '''Expresion : Expresion PUNTO LENGTH'''
    p[0]=Expresion6(p[1])

def p_ExpresionB(p):
	'''Expresion : Expresion binary Expresion'''
	p[0] = ExpresionB(p[1],p[2],p[3])

def p_Expresion7(p):
    '''Expresion : Unary Expresion'''
    p[0]=Expresion8(p[1], p[2])

def p_binary(p):
    '''binary : MAS 
               | MENOS
               | MULTI 
               | DIVISION 
               | MODULO 
               | AND 
               | OR 
               | MENOR 
               | MENORIG 
               | MAYOR 
               | MAYORIG 
               | COMPARAR 
               | DIFERCOMP'''
    p[0]=Exp_Bin(p[1])




def p_Unary(p):
    '''Unary : MENOS
             | DIFER'''
    p[0]=Unary(p[1])

def p_Expresion8(p):
    '''Expresion : Literal'''
    p[0]=Expresion9(p[1])

def p_Literal(p):
    '''Literal :  TRUE
                | CADENA
                | FALSE
                | NULL
                | ENTNUM'''
    p[0]=Literal(p[1])    

def p_Expresion9(p):
    '''Expresion : PARENIZQ Expresion PARENDER'''
    p[0]=Expresion10(p[2])    

def p_vacio(p):
    '''vacio :'''
    pass

#Manejo de errores
    
def p_error(p):
    print("Error de sintaxis en: '%s'" % p)
    print("Linea: '%s'" %  p.lineno)
    print("Posicion: '%s'" % p.lexpos)
    
yacc.yacc(method='LALR')

#s = open("C:\\Users\\sebas\\Desktop\\final Compiladores\\Analizador Sintactico\\test\\prueba_decVar.MJ").read()
s = open("C:\\Users\\sebas\\Desktop\\final Compiladores\\Analizador Sintactico\\test\\ejemplo1.MJ").read()
#s = open("C:\\Users\\sebas\\Desktop\\final Compiladores\\Analizador Sintactico\\test\\pruebaStmt.MJ").read()
#s = open("C:\\Users\\sebas\\Desktop\\final Compiladores\\Analizador Sintactico\\test\\hola.mj").read()

raiz = yacc.parse(s)
#raiz.preOrden()
print (raiz.traducir())