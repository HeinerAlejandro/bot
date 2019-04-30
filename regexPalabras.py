
#import models.py
# Metodos del modelo
#pronombreInterrogativos = WordsRegex.objects.all().filter(wordsType = 'PI')
#verbosP =  WordsRegex.objects.all().filter(wordsType = 'V')
#sujetos =  WordsRegex.objects.all().filter(wordsType = 'S')
pronombreInterrogativos =[
       r"qui[eé]n(\S*)",
       r'qu[eé](\S*)',
       r'cu[aá]l(\S*)',
       r'cu[aá]nt(\S*)', 
       r'c[oó]mo(\S*)',
       r'd[oó]nde(\S*)',
       r'cu[aá]ndo(\S*)',
       r'por\squ[eé]']

verbosP=[       
                 r"pued(\S*)|permite(\S*)|acepta(\S*)", #reglas
                 r"ofrece(\S*)|tien(\S+)|hay(\S*)|han|hace",r"traer",r"vende(\S*)|compra(\S*)",
                 r"ocurri(\S+)",
                 r"reservar|apartar|alquiler(\S*)", #inventario
                 r"recomiendan|sugiere(\S*)|aconseja(\S*)", r"divert(\S*)",             #oferta
                 r"est[aá](\S*)", r"\sser|\sson|\ses|\sese|\sest[aá]|\sest(\S*)",
                 r"informar(\S*)|notifica|contact(\S*)",
                 r"nadar|bañar(\S*)", r"comer(\S*)|alimentar(\S*)",#acciones 
                 r"encontra(\S*)|encuentro|ubico|ubicar(\S*)" ,
                 r"abrir(\S*)|abren|cerrar|cierran(\S*)" ,
                 r"funcionan"
            ]  


sujetos = [
          r"informac(\S*)", r"duda(\S*)", r"consej(\S*)", r"horario|hora\S*|tiempo", r"seguridad|aseguran|precauci[oó]n(\S*)", 
          #Relacionado con el negocio
          r"aseo(\S*)|baño(\S*)", r"encargado(\S*)", "ambulancia|primeros auxilios",
          r"servicio(\S*)", r"actividad(\S*)", r"festividad(\S*)", "reservac",
          #objeto del negocio
          r"pelota|juguete|coroto", r"mesa(\S*)|un lugar", r"ubica(\S*)|localiza", "cocina(\S*)|parrilla(\S*)"
          r"parque(\S*)",  r"r[ií]o(\S*)" ,"art[ií]culo|cosa(\S*)|producto(\S*)", r"comida|alimento(\S*)|bebida(\S*)" , r"pi(s*)cina(\S*)",
          #clientes
          r"niño(\S*)|caraj(\S*)",r"adult(\S*)", r"persona(s*) mayor(es*)(\S*)", r"anciano(\S*)" ,"personas",
               r"mascota|mascotas|perro(\S*)", r"afuera"
]
