#Defino la lista numeros_aleatorios
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

#Calculo la moda, la mediana y la media de los numeros pertenecientes a la variable numeros_aleatorios
from statistics import mode, median, mean
moda = mode (numeros_aleatorios)
mediana = median (numeros_aleatorios)
media = mean (numeros_aleatorios)
if media > mediana > moda:
    print ("Hay sesgo positivo")
elif media < mediana < moda:
    print ("Hay sesgo negativo")
elif media == mediana == moda:
    print ("No hay sesgo")
else:
    print ("No se puede determinar el sesgo ya que no se puede predecir la forma de una distribución normal")