#operaciones con numeros complejos
#suma
n_complejo_1 = 6 + 7j #
n_complejo_2 = 19 - 47j #

adicion = n_complejo_1 + n_complejo_2 #suma

print(adicion)
#resta
n_complejo_1 = 9 + 3j #
n_complejo_2 = 25 - 15j #

sustraccion = n_complejo_1 - n_complejo_2 #resta

print(sustraccion)
#multiplicacion
n_complejo_1 = 5 + 4j #
n_complejo_2 = 20 - 11j

multiplicacion = n_complejo_1 * n_complejo_2 #multiplicacion

print(multiplicacion)

#divicion
n_complejo_1 = 2 + 4j #
n_complejo_2 = 26 - 18j

division = n_complejo_1 / n_complejo_2

print(division)

#conjugado

a = 120 + 4j
print(a.conjugate()) #(1-1j)

#modulo

a = (40 + 4j)
abs (a)
print (abs(a))

#polar a cartesiano
import math
def polar_cartesiano(a):

    real = round(a[0] * math.cos(a[1]))
    img = round(a[0] * math.sin(a[1]))
    return real,img
#
def Rfase(a):

    if a[0] < 0 and a[1] < 0:
        phase = round(2 * math.pi - (-1 * (math.atan2(a[1], a[0]))), 2)
        return phase
    elif a[0] > 0 > a[1]:
        phase = round((2 * math.pi + math.atan2(a[1], a[0])), 2)
        return phase
    else:
        phase = round((math.atan2(a[1], a[0])), 2)
        return phase


def main():
    a = (20,80)
    print(polar_cartesiano((a)))
    print(Rfase(a))
main()