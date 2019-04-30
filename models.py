from django.db import models

# Modelo de la base de datos del bot

#La palabras tienen tres posibles categorias dentro del vocabulario del bot Sujeto, verbo y Pronombre interrogativo.
# Las preguntas tienen dos extructuras gramaticales
# verbo + sujeto
# pronombre interrogativo + verbo + sujeto
categories = (
    ('S', 'sujeto'),
    ('V', 'verbo'),
    ('PI', 'pronombre Interrogativo')
)

# 

## Palabras 
# Expresion regular de un conjunto de palabras, Muchos sustantivos tienen sinonimos al igual que los verbos
class WordsRegex(models.Model):

    wRegex = models.CharField(verbose_name = 'Regex Palabra', max_length= 100)
    wordsType = models.CharField( max_length=2, choices = categories)

    def __str__(self):
        return self.wRegex

    def addword(self, word):
        self.wRegex = self.wRegex + '|' + word

    def removeword(self, regexword):
        self.wRegex = self.wRegex.replace('|'+ regexword, '')

#supercalifragilisticoespialidoso tiene 32 caracteres
    

# Respuesta
class Reply(models.Model):

    replyRegex = models.CharField(verbose_name = 'Expresion regular de la respuesta' ,max_length=150, primary_key=True )
    replyText = models.CharField(verbose_name = 'Texto de la respuesta',max_length=150 )

    def __str__(self):
        return self.replyText

    def setReplyText(self, newText):
        self.replyText = newText
    
    
