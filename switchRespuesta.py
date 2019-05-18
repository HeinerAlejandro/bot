
from ..models import Reply

charla = Reply.objects.all()

class Switcher(object):
       
    def posibles_respuestas(self, pregunta):
        print (pregunta)

        respuesta = "No le entiendo, podria ser mas claro en su explicacion"
        try:

            respuesta = charla.get(replyRegex =  pregunta)

            return respuesta.replyText

        except Exception:
            pass

        return respuesta
        

    
