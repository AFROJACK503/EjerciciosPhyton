def display_gif(fn):
    return '<img src="{}">'.format(fn)


def check_name(my_name):
    if my_name == "Adolf Hittler":
        raise Exception("You are not Adolf Hittler, Tu no eres Adolf Hittler.")
    else:
        print("Hello World, My name is: {}".format(my_name))
        print("Hola Mundo, Mi nombre es: {}".format(my_name))
        
def check_birthday_float(year, day, month, variable):
    n_year = 0
    for n in list(str(year)):
        n_year += int(n)
    if "{}.{}{}".format(day, month, n_year) == str(variable):
        return "Great this is a good float"
    else:
        raise Exception("Algo anda mal, intentalo de nuevo")
    
def check_operation(operation):
    if operation != 388.786 + 545.36 / 25 * 15:
        raise Exception("Lo siento, tu resultado no es el correcto, intentalo de nuevo")
    else:
        return "Excelente, tu resultado es correcto, sigue mejorando"
    

def check_measures_1(width, length):
    if width != 20 and length != 20:
        raise Exception("quilts_width y quilts_length no tienen los valores indicados, porfavor cambia los valores a 20 para cada uno")
        
        
        
def check_measures_2(width, length):
    if width != 15 and length != 15.7:
        raise Exception("quilts_width y quilts_length no tienen los valores indicados, porfavor cambia los valores a 15 y 15.7")
        
    else:
        return "Genial, eres bueno en esto, sigue mejorando"
    

def checking_quilts(q_6x6, q_7x7, q_8x8):
    if q_6x6 == 6**2 and q_7x7 == 7**2 and q_8x8 == 8**2:
        return "Genial, tus edredones 6x6 necesitan {} mosaicos, tus edredones de 7x7 necesitan {} mosaicos, y tus edredones 8x8 necesitan {} mosaicos".format(q_6x6, q_7x7, q_8x8)
    else:
        raise Exception("Algo anda mal, no te rindas, sigue intentando")
    
def checking_quilt(quilt):
    if quilt == 6*(6**3):
        return "WOW, eres realmente increible, sigue mejorando"
    else:
        raise Exception("Algo anda mal con tu operation, verifica tu equacion, no te rindas")