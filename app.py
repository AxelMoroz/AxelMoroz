# Lista para almacenar los productos
productos = []

# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
    # AQUÍ PUEDES COMENZAR A DESARROLLAR LA SOLUCIÓN
    
    while True:
        # Mostrar el menú principal
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            # Agregar un producto al inventario
            nombre = input("Ingrese el nombre del producto: ").strip()
            
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa. Intente de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            
            # Agregar producto como lista [nombre, cantidad] a productos
            productos.append([nombre, cantidad])
            print("Producto agregado con éxito.")
        
        elif opcion == "2":
            # Mostrar productos en el inventario
            if len(productos) == 0:
                print("No hay productos registrados.")
            else:
                print("\n--- Inventario Actual ---")
                indice = 1
                for producto in productos:
                    print(f"{indice}. Producto: {producto[0]}, Cantidad: {producto[1]}")
                    indice += 1
        
        elif opcion == "3":
            # Salir del sistema
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            # Opción inválida
            print("Opción inválida. Por favor, intente de nuevo.")

# Llamar a la función principal (NO ELIMINAR)
if __name__ == "__main__":
    main()
1