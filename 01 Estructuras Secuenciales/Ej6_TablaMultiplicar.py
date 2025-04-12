numero = float (input("Ingrese un número: "))
print(f"La tabla de multiplicar de {numero} es: ")
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")