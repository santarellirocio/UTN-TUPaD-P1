# Diccionario inicial de productos
stock_productos = {"mesas": 10, "sillas": 45, "sillones": 8}

# Solicitar producto al usuario
producto = input("Ingresá el nombre del producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = input("¿Querés agregar unidades a este producto? (si/no): ").lower()
    if agregar == "si":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    print(f"{producto} no está en el inventario.")
    nuevo = input("¿Querés agregarlo como nuevo producto? (si/no): ").lower()
    if nuevo == "si":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = cantidad
        print(f"{producto} fue agregado con {cantidad} unidades.")

# Mostrar el inventario actualizado
print("\nInventario final:")
for prod, stock in stock_productos.items():
    print(f"{prod}: {stock}")