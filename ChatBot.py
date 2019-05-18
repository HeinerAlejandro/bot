import string
import re #Expresiones regulares
from .. import models
from . import switchRespuesta


#import models
#define las posibles respuestas del bot 
#pronombreInterrogativos = WordsRegex.objects.all().filter(wordsType = 'PI')
#verbosP =  WordsRegex.objects.all().filter(wordsType = 'V')
#sujetos =  WordsRegex.objects.all().filter(wordsType = 'S')

class ChatBot(object):

    #Variables
    vocabulario = {}
    responde ={ 1: switchRespuesta.Switcher().posibles_respuestas}
    configurable = False

    def __init__(self, nombre):
        Exception("despues de construct")
        self.vocabulario = { 
                "V":list(map(lambda x:re.compile(x.wRegex, re.IGNORECASE), models.WordsRegex.objects.all().filter(wordsType = 'V'))) ,
                "PI":list(map(lambda x:re.compile(x.wRegex, re.IGNORECASE), models.WordsRegex.objects.all().filter(wordsType = 'PI'))),
                "S": list(map(lambda x:re.compile(x.wRegex, re.IGNORECASE), models.WordsRegex.objects.all().filter(wordsType = 'S')))
                }
        self.nombre = nombre

   
#------------------------------------Funciones 
   
    #Analizadores lexicos: tienen como funcion recibir un mensaje 
    #categoriazaran las palabras por medio de expresiones regulares 
    # y devolveran la expresion regular que localizo dicha palabra.

    #Entrada: 
    #   mensaje: Es el texto que recibira por parte del usuario
    #Salida:
    #   regex: expresion regular que el analizador lexico utilizo para localizar la palabra

    def busquedaPVerbo (self, mensaje):
        verbos = ""
        for i in self.vocabulario["V"]:
            result=i.search(mensaje)
            if( result != None):
                verbos = verbos + result.re.pattern + "|"
        return verbos

    def busquedaSujeto (self, mensaje):
        for i in self.vocabulario["S"]:
            result=i.search(mensaje)
            if( result != None):
                return result.re.pattern + "|"
        return ""

    def busquedaPronombreInterrogativo (self, mensaje):
        for i in self.vocabulario["PI"]:
            result= i.search(mensaje)
            if( result != None):
                return result.re.pattern + "|"
        return ""

#-----------------------------Metodos propios del bot

    #Escucha: Recibe el mensaje realiza llamadas a los distintos analizadores. 
    #Concatena esa respuesta en una unica variable que sera retornada.
    def escucha(self,mensaje):
        msg = self.busquedaPronombreInterrogativo ( mensaje ) + self.busquedaPVerbo (mensaje) + self.busquedaSujeto(mensaje)
        return msg

    #Habla: 
    #Primero llama a la funcion escucha y obtiene un String que representa  
    #a la concatenacion de las expresiones regulares
    # Posteriormente se llama a la variable respondea que es un switcher que retornara
    # la respuesta a la pregunta del usuario
    def habla(self, mensaje ):
        regexPregunta = self.escucha( mensaje)
        msgRespuesta = self.responde[1]( regexPregunta )
        return msgRespuesta
    

    # Esto es para agregarle nuevas palabras del bot... Aun estoy trabajando con ello XD
    def AgregarRespueta(self):
        return 
    
    def setConfigurable (self, nV):
            self.configurable = nV

#----------------------------------------------------------Soy un bot -----------------------------------------------------------------


