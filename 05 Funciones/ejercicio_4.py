import utils
# Solicitamos al usuario el radio del círculo
radio = float (input("Ingrese el radio del círculo: "))

# Mostramos los resultados de área y perímetro llamando a la función para mostrar el resultado 
print (f"El área del círculo de radio {radio} es: {utils.calcular_area_circulo(radio)} y su perimetro es: {utils.calcular_perimetro_circulo(radio)}")