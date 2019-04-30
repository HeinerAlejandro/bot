
from ..bot import dialogoBot

charla = dialogoBot.dialogo

class Switcher(object):
       
    def posibles_respuestas(self, pregunta):
        print (pregunta)
        respuesta = charla.get(pregunta, "No le entiendo, podria ser mas claro en su explicacion")
        return respuesta

    
