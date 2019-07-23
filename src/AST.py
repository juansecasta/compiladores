
cont = 0
def incrementarContador():
    global cont 
    cont += 1
    return "%d " % cont

class Node: 

    pass

class Programa(Node):
    def __init__(self, ProgramaDecl):
        self.ProgramaDecl = ProgramaDecl
        self.Nombre="inicio_del_Programa"
    
    def preOrden(self):
        print self.Nombre
        self.ProgramaDecl.preOrden("\t")

    def traducir(self):
        self.id = incrementarContador()
        (self.ProgramaDeclT, self.dtxt) = self.ProgramaDecl.traducir()
        self.txt = self.dtxt
        self.txt += self.id + " [label= "+self.Nombre+", shape=box]\n\t"
        self.txt += self.id + " -> " + self.ProgramaDeclT + "\n\t"
        return "digraph G {\n"+self.txt+"\n}"  

    
class ProgramaDecl(Node): 
    """Lista las clases"""
    def __init__(self, classDecl, ProgramaDecl):
        self.classDecl = classDecl
        self.ProgramaDecl = ProgramaDecl
        self.Nombre="List_Decl_Clases "
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.classDecl.preOrden(ident)
        self.ProgramaDecl.preOrden(ident)    

    def traducir(self):
        self.id = incrementarContador()
        (self.classDeclt, self.ctxt) = self.classDecl.traducir()
        (self.ProgramaDeclT, self.dtxt) = self.ProgramaDecl.traducir()            
        self.txt = self.ctxt
        self.txt += self.dtxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"
        self.txt += self.id + ' -> ' + self.classDeclt + '[color="0.515 0.762 0.762"] \n\t'
        self.txt += self.id + " -> " + self.ProgramaDeclT + "\n\t"        

        return (self.id, self.txt)

class Declaracion_Clase(Node):
    def __init__(self, ID, Extends_Op, Declaracion_Atributos_P):
        self.ID = ID
        self.Extends_Op = Extends_Op
        self.Declaracion_Atributos_P = Declaracion_Atributos_P
        self.Nombre="Declaracion_de_Clase"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Extends_Op.preOrden(ident)
        self.Declaracion_Atributos_P.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Extends_OpT, self.ctxt) = self.Extends_Op.traducir()
        (self.Declaracion_Atributos_PT, self.dtxt) = self.Declaracion_Atributos_P.traducir()            
        self.txt = self.ctxt
        self.txt += self.dtxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"
        self.txt += self.id + ' -> ' + self.Extends_OpT + '[color="0.515 0.762 0.762"] \n\t'
        self.txt += self.id + " -> " + self.Declaracion_Atributos_PT + "\n\t"        

        return (self.id, self.txt)

class ExtendsOp(Node):
    def __init__(self, ID):
        self.ID = ID
        self.Nombre="Extends"
        self.txt = ""
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"

    def traducir(self):        
        self.id = incrementarContador()
        self.txt += self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)   
       

    
class Declaracion_Atributos_P(Node):
    def __init__(self, Declaracion_Atributos, Declaracion_Atributos_P):
        self.Declaracion_Atributos = Declaracion_Atributos
        self.Declaracion_Atributos_P = Declaracion_Atributos_P
        self.Nombre = "Declaracion_de_Atributos"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        self.ident = ident + "\t"
        self.Declaracion_Atributos.preOrden(ident)
        self.Declaracion_Atributos_P.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Declaracion_AtributosT, self.ttxt) =self.Declaracion_Atributos.traducir()
        (self.Declaracion_Atributos_PT, self.btxt) =self.Declaracion_Atributos_P.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Declaracion_AtributosT + "\n\t"
        self.txt += self.id + " -> " + self.Declaracion_Atributos_PT + "\n\t"
        return (self.id, self.txt)        
       


class Declaracion_Atributos(Node):
    def __init__(self, Type, ID, ListComaID):
        self.Type = Type
        self.ID = ID
        self.ListComaID = ListComaID
        self.Nombre = "Declaracion_de_Campo"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Type.preOrden(ident)
        self.ListComaID.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.TypeT, self.ttxt) =self.Type.traducir()
        (self.ListComaIDT, self.btxt) =self.ListComaID.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.TypeT + "\n\t"
        self.txt += self.id + " -> " + self.ListComaIDT + "\n\t"
        return (self.id, self.txt)           
        

class Declaracion_Campo_P(Node):
    def __init__(self, ID, ListComaID):
        self.ID = ID
        self.ListComaID = ListComaID
        self.Nombre = "lista_coma_id_fieldDecl"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Declaracion_Campo_P.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ListComaIDT, self.ttxt) =self.ListComaID.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ListComaIDT + "\n\t"
        
        return (self.id, self.txt)                   


class Declaracion_Atributos_P3(Node):
    def __init__(self, Tipo_Metodo, ID, Formales_P, Bloque):
        self.Tipo_Metodo = Tipo_Metodo
        self.ID = ID
        self.Formales_P = Formales_P
        self.Bloque = Bloque
        self.Nombre = "Declaracion_Metodo"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + " " + self.ID
        ident = ident + "\t"
        self.Tipo_Metodo.preOrden(ident)
        self.Formales_P.preOrden(ident)
        self.Bloque.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Formales_PT, self.ttxt) =self.Formales_P.traducir()
        (self.BloqueT, self.btxt) =self.Bloque.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Formales_PT + "\n\t"
        self.txt += self.id + " -> " + self.BloqueT + "\n\t"
        return (self.id, self.txt)           

        

class Declaracion_Atributos_P4(Node):
    def __init__(self, ID, Formales_P, Bloque):
        self.ID = ID
        self.Formales_P = Formales_P
        self.Bloque = Bloque
        self.Nombre = "Declaracion_Metodo_void"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + " " + self.ID
        ident = ident + "\t"
        self.Formales_P.preOrden(ident)
        self.Bloque.preOrden(ident)

    def traducir(self):

        self.id = incrementarContador()
        (self.Formales_PT, self.ttxt) =self.Formales_P.traducir()
        (self.BloqueT, self.btxt) =self.Bloque.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Formales_PT + "\n\t"
        self.txt += self.id + " -> " + self.BloqueT + "\n\t"
        return (self.id, self.txt)              



class Formales_P(Node):
    def __init__(self, Type, ID, Formales_PP):
        self.Type = Type
        self.ID = ID
        self.Formales_PP = Formales_PP
        self.Nombre = "Formales"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Type.preOrden(ident)
        self.Formales_PP.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Formales_PPT, self.ttxt) =self.Formales_PP.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Formales_PPT + "\n\t"
        
        return (self.id, self.txt)               



class Formales_P3(Node):
    def __init__(self, Type, ID, Formales_PP):
        self.Type = Type
        self.ID = ID
        self.Formales_PP = Formales_PP
        self.Nombre = "Formales_opcional"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Type.preOrden(ident)
        self.Formales_PP.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Formales_PPT, self.ttxt) =self.Formales_PP.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Formales_PPT + "\n\t"
        
        return (self.id, self.txt)               



class Type(Node):
    def __init__(self, Tipo):
        self.Tipo = Tipo
        
    def preOrden(self, ident):
        print ident + self.Tipo
        ident = ident + "\t" 

    def traducir(self):
        self.id = incrementarContador()        
        self.txt = self.id +" [label= type]\n\t"
        return (self.id, self.txt)              

class Type1(Node):
    def __init__(self, Tipo):
        self.Tipo = Tipo
        
    def preOrden(self, ident):
        print ident + self.Tipo
        ident = ident + "\t"  
        self.Tipo.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()        
        self.txt = self.id +" [label= type]\n\t"
        return (self.id, self.txt)            

class Bloque1(Node):
    def __init__(self, Bloque_P2, Bloque_P3):
        self.Bloque_P2 = Bloque_P2
        self.Bloque_P3 = Bloque_P3
        self.Nombre = "Bloque"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Bloque_P2.preOrden(ident)
        self.Bloque_P3.preOrden(ident)

    def traducir(self):
        #global txt
        self.id = incrementarContador()
        (self.Bloque_P2T, self.ttxt) =self.Bloque_P2.traducir()
        (self.Bloque_P3T, self.btxt) =self.Bloque_P3.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Bloque_P2T + "\n\t"
        self.txt += self.id + " -> " + self.Bloque_P3T + "\n\t"
        return (self.id, self.txt) 


class Bloque2(Node):
    def __init__(self, Declaracion_Variable, Bloque_P2):
        self.Declaracion_Variable = Declaracion_Variable
        self.Bloque_P2 = Bloque_P2
        self.Nombre = "Bloque_Decl_Variables"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Declaracion_Variable.preOrden(ident)
        self.Bloque_P2.preOrden(ident)
        
    def traducir(self):
        self.id = incrementarContador()
        (self.Declaracion_VariableT, self.ttxt) =self.Declaracion_Variable.traducir()
        (self.Bloque_P2T, self.btxt) =self.Bloque_P2.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Declaracion_VariableT + "\n\t"
        self.txt += self.id + " -> " + self.Bloque_P2T + "\n\t"
        return (self.id, self.txt)         


class Declaracion_Variable(Node):
    def __init__(self, Type,ID,IgualExp, IDAsign):

        self.ID = ID
        self.Type = Type
        self.IgualExp = IgualExp
        self.IDAsign = IDAsign
        self.Nombre = "Declaracion_Variable"

        
    def preOrden(self, ident):
        print ident + self.Nombre + " : "+ self.ID
        self.Type.preOrden(ident)
        self.IgualExp.preOrden(ident)
        self.IDAsign.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.TypeT, self.ttxt) =self.Type.traducir()
        (self.IgualExpT, self.btxt) =self.IgualExp.traducir()
        (self.IDAsignT, self.ctxt) =self.IDAsign.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        self.txt+=self.ctxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.TypeT + "\n\t"
        self.txt += self.id + " -> " + self.IgualExpT + "\n\t"
        self.txt += self.id + " -> " + self.IDAsignT + "\n\t"
        return (self.id, self.txt)         

        

class IgualExp(Node):
    def __init__(self,Expresion):
        self.Expresion = Expresion
        self.Nombre = "asignacion_a_variable"

    def preOrden(self,ident):
        ident = ident + "\t"
        print ident + self.nombre 
        self.Expresion.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"        
        return (self.id, self.txt)


class Asignar_Valor3(Node):
    def __init__(self, ID, Expresion, Asignar_Valor):
        self.ID = ID
        self.Expresion = Expresion
        self.Asignar_Valor = Asignar_Valor
        self.Nombre = "Declaracion_Variable"
        
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.Asignar_Valor.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.Asignar_ValorT, self.btxt) =self.Asignar_Valor.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.Asignar_ValorT + "\n\t"
        return (self.id, self.txt)      

class Bloque4(Node):
    def __init__(self, stmt, Bloque_P3):
        self.stmt = stmt
        self.Bloque_P3 = Bloque_P3
        self.Nombre = "Bloque"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.stmt.preOrden(ident)
        self.Bloque_P3.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.stmtT, self.ttxt) =self.stmt.traducir()
        (self.Bloque_P3T, self.btxt) =self.Bloque_P3.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.stmtT + "\n\t"
        self.txt += self.id + " -> " + self.Bloque_P3T + "\n\t"
        return (self.id, self.txt)           

class stmt(Node):
    def __init__(self, Assign):
        self.Assign= Assign
        self.Nombre = "Asignacion"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Assign.preOrden(ident)
        
    def traducir(self):
        self.id = incrementarContador()
        (self.AssignT, self.ttxt) =self.Assign.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.AssignT + "\n\t"        
        return (self.id, self.txt)   
    

class stmt2(Node):
    def __init__(self, Call):
        self.Call= Call
        self.Nombre = "Llamado"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Call.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.CallT, self.ttxt) =self.Call.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.CallT + "\n\t"        
        return (self.id, self.txt)          
       


class stmt3(Node):
    def __init__(self, Expresion_P):
        self.Expresion_P= Expresion_P
        self.Nombre = "Return"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion_P.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Expresion_PT, self.ttxt) =self.Expresion_P.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Expresion_PT + "\n\t"        
        return (self.id, self.txt)           
        
class stmt4(Node):
    def __init__(self):
        self.Nombre = "Return"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"

    def traducir(self):        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        
        

class stmt5(Node):
    def __init__(self, Expresion, stmt, stmt1):
        self.Expresion= Expresion
        self.stmt= stmt
        self.stmt1= stmt1
        self.Nombre = "Stmt"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.stmt.preOrden(ident)
        self.stmt1.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.stmtT, self.btxt) =self.stmt.traducir()
        (self.stmt1T, self.ctxt) =self.stmt1.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        self.txt+=self.ctxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.stmtT + "\n\t"
        self.txt += self.id + " -> " + self.stmt1T + "\n\t"
        return (self.id, self.txt)        


class stmt6(Node):
    def __init__(self, Expresion, stmt):
        self.Expresion= Expresion
        self.stmt= stmt
        self.Nombre = "Stmt"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.stmt.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        self.txt =""
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.stmtT, self.btxt) =self.stmt.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.stmtT + "\n\t"
        return (self.id, self.txt)                  

 

class stmt7(Node):
    def __init__(self, Expresion, stmt):
        self.Expresion= Expresion
        self.stmt= stmt
        self.Nombre = "Stmt"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.stmt.preOrden(ident)
        
    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.stmtT, self.btxt) =self.stmt.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.stmtT + "\n\t"
        return (self.id, self.txt)  
    

class stmt8(Node):
    def __init__(self, BREAK_O_CONTINUE):
        self.BREAK_O_CONTINUE= BREAK_O_CONTINUE
        self.Nombre = "Break_o_Continue"
        self.txt = ""
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"

    def traducir(self):       
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)                


class stmt9(Node):
    def __init__(self, Bloque):
        self.Bloque= Bloque
        self.Nombre = "Bloque"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Bloque.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.BloqueT, self.ttxt) =self.Bloque.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.BloqueT + "\n\t"        
        return (self.id, self.txt) 

class Asignacion(Node):
    def __init__(self, Location, Expresion):
        self.Location = Location
        self.Expresion = Expresion
        self.Nombre = "Asignacion2"

    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Location.preOrden(ident)
        self.Expresion.preOrden(ident)
        
    def traducir(self):
        self.id = incrementarContador()
        (self.LocationT, self.ttxt) =self.Location.traducir()
        (self.ExpresionT, self.btxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.LocationT + "\n\t"
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        return (self.id, self.txt)  

class location1(Node):
    def __init__(self, ID):
        self.ID = ID
        self.Nombre = "Variable"
                
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"

    def traducir(self):
        self.txt = ""       
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)   

class Location2(Node):
    def __init__(self, Expresion, ID):
        self.Expresion = Expresion
        self.ID = ID
        self.Nombre = "Variable"
                
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        self.Expresion.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"        
        return (self.id, self.txt)        

class Location3(Node):
    def __init__(self, Expresion, Expresion2):
        self.Expresion = Expresion
        self.Expresion2 = Expresion2
        self.Nombre = "Variable"
        
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.Expresion2.preOrden(ident)
        
    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.Expresion2T, self.btxt) =self.Expresion2.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.Expresion2T + "\n\t"
        return (self.id, self.txt)        


class Llamado(Node):
    def __init__(self, Metodo, Actuales):
        self.Metodo = Metodo
        self.Actuales_P = Actuales_P
        self.Nombre = "Llamado1"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Metodo.preOrden(ident)
        self.Actuales_P.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.MetodoT, self.ttxt) =self.Metodo.traducir()
        (self.ActualesT, self.btxt) =self.Actuales.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.MetodoT + "\n\t"
        self.txt += self.id + " -> " + self.ActualesT + "\n\t"
        return (self.id, self.txt)          


class Llamado1(Node):
    def __init__(self, Metodo):
        self.Metodo = Metodo
        self.Nombre = "Llamado1"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Metodo.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.MetodoT, self.ttxt) =self.Metodo.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.MetodoT + "\n\t"        
        return (self.id, self.txt)          


class Metodo(Node):
    def __init__(self, ID):
        self.ID = ID
        self.Nombre = "Metodo"
                
    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.ID
        ident = ident + "\t"
        
    def traducir(self):        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        


class Metodo_P(Node):
    def __init__(self, Expresion, ID):
        self.Expresion = Expresion
        self.ID = ID
        self.Nombre = "Metodo"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"        
        return (self.id, self.txt)          


class Actuales(Node):
    def __init__(self, Expresion, Actuales_PP):
        self.Expresion = Expresion
        self.Actuales_PP = Actuales_PP
        self.Nombre = "Actuales"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.Actuales_PP.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.Actuales_PPT, self.btxt) =self.Actuales_PP.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.Actuales_PPT + "\n\t"
        return (self.id, self.txt)          


class Actuales_PP(Node):
    def __init__(self, Expresion, Actuales_PP):
        self.Expresion = Expresion
        self.Actuales_PP = Actuales_PP
        self.Nombre = "Actuales"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident)
        self.Actuales_PP.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        (self.Actuales_PPT, self.btxt) =self.Actuales_PP.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        self.txt += self.id + " -> " + self.Actuales_PPT + "\n\t"
        return (self.id, self.txt)           
       

class Expresion1(Node):
    def __init__(self, Location):
        self.Location = Location
        self.Nombre = "Expresion"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Location.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.LocationT, self.ttxt) =self.Location.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.LocationT + "\n\t"        
        return (self.id, self.txt)          

class f(Node):
    def __init__(self, Call):
        self.Call = Call
        self.Nombre = "Expresion"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Call.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.CallT, self.ttxt) =self.Call.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.CallT + "\n\t"        
        return (self.id, self.txt)          

        

class Expresion2(Node):
    def __init__(self, Call):
        self.Call = Call
        self.Nombre = "Expresion"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Call.preOrden(ident)


    def traducir(self):
        self.id = incrementarContador()
        (self.CallT, self.ttxt) =self.Call.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.CallT + "\n\t"        
        return (self.id, self.txt)         
        
class Expresion3(Node):
    def __init__(self, THIS):
        self.THIS = THIS
        self.Nombre = "This"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"

    def traducir(self):        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        

class Expresion4(Node):
    def __init__(self, NEW, ID):
        self.NEW = NEW
        self.ID = ID
        self.Nombre = "New"
        self.txt = ""
                
    def preOrden(self, ident):
        print ident + self.Nombre + " " + self.ID
        ident = ident + "\t"

    def traducir(self):        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)          
                

class Expresion5(Node):
    def __init__(self, Type, Expresion):
        self.Type = Type
        self.Expresion = Expresion
        self.Nombre = "New_Type"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Type.preOrden(ident)
        self.Expresion.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.TypeT, self.ttxt) =self.Type.traducir()
        (self.ExpresionT, self.btxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.TypeT + "\n\t"
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        return (self.id, self.txt)           

class Expresion6(Node):
    def __init__(self, Expresion):
        self.Expresion = Expresion
        self.Nombre = "Expresion"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Expresion.preOrden(ident) 

    def traducir(self):
        self.id = incrementarContador()
        (self.ExpresionT, self.ttxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"        
        return (self.id, self.txt)                

class ExpresionB(Node):
    def __init__(self, Expresion1, Binario, Expresion2):
        self.Expresion1 = Expresion1
        self.Binario = Binario
        self.Expresion2 = Expresion2
        self.Nombre  = "Expresion_Binaria"

    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"        
        self.Expresion1.preOrden(ident)
        self.Binario.preOrden(ident)
        self.Expresion2.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.Expresion1T, self.ttxt) =self.Expresion1.traducir()
        (self.BinarioT, self.btxt) =self.Binario.traducir()
        (self.Expresion2T, self.ctxt) =self.Expresion2.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        self.txt+=self.ctxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.Expresion1T + "\n\t"
        self.txt += self.id + " -> " + self.BinarioT + "\n\t"
        self.txt += self.id + " -> " + self.Expresion2T + "\n\t"
        return (self.id, self.txt)           

class Exp_Bin(Node):
    def __init__(self, Binario):
        self.Binario = Binario
        self.Nombre = "Expresion_Binario"
        
    def preOrden(self, ident):
        print ident + self.Nombre + " : "+self.Binario
        ident = ident + "\t"

    def traducir(self):
        self.txt = ""
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        

class Expresion8(Node):
    def __init__(self,Unary, Expresion):
        self.Unary = Unary
        self.Expresion = Expresion
        self.Nombre = "Expresion_Unaria"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Unary.preOrden(ident)
        self.Expresion.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.UnaryT, self.ttxt) =self.Unary.traducir()
        (self.ExpresionT, self.btxt) =self.Expresion.traducir()
        self.txt=self.ttxt
        self.txt+=self.btxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.UnaryT + "\n\t"
        self.txt += self.id + " -> " + self.ExpresionT + "\n\t"
        return (self.id, self.txt)         
       

class Unary(Node):
    def __init__(self, Unario):
        self.Unario = Unario
        
    def preOrden(self, ident):
        print ident + 'Expresion: ' + self.Unario
        ident = ident + "\t"

    def traducir(self):        
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        


class Expresion9(Node):
    def __init__(self,Literal):
        self.Literal = Literal
        self.Nombre = "Expresion_Literal"
                
    def preOrden(self, ident):
        print ident + self.Nombre
        ident = ident + "\t"
        self.Literal.preOrden(ident)

    def traducir(self):
        self.id = incrementarContador()
        (self.LiteralT, self.ttxt) =self.Literal.traducir()
        self.txt=self.ttxt
        
        self.txt += self.id + " [label= "+self.Nombre+"]\n\t"        
        self.txt += self.id + " -> " + self.LiteralT + "\n\t"        
        return (self.id, self.txt)       


class Literal(Node):
    def __init__(self, Tipo):
        self.Tipo = Tipo
        self.Nombre = "literal"
        
        
    def preOrden(self, ident):
        print ident + 'Expresion: '+ str(self.Tipo)
        ident = ident + "\t"        

    def traducir(self):
        self.txt = ""        
        self.id = incrementarContador()
        self.txt += self.id +" [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)   


class DeclListNull(Node): 
    """ Lista null para terminar la recursividad 
        Utilizar NodeList (para disminuir la profundidad del arbol 
    """
    def __init__(self):
        self.Nombre="null"        
        
    def preOrden(self,ident):
        #print ident + 'lista de declaracion null'
        print ident + self.Nombre

    def traducir(self):
       
        self.id =incrementarContador()
        self.txt = self.id + " [label= "+self.Nombre+"]\n\t"
        return (self.id, self.txt)        

class Numeros(Node):
    def __init__(self,Numero):
        self.Numero = Numero
        self.Nombre = "Numero"

    def preOrden(self, ident):
        print ident + self.Nombre + ": " + self.Numero
        ident = ident + "\t"

    def traducir(self): 
              
        self.id = incrementarContador()
        self.txt+=self.id +" [label= "+self.name+"]\n\t"
        return (self.id, self.txt)        



