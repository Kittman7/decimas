#Articulo
precio = float(input("Ingrese el precio del artículo: "))


es_estudiante = input("¿Tiene descuento? (si/no): ")
es_cliente_frecuente = input("Es cliente frecuente? (si/no):")



if es_estudiante == 'si':
    estudian_descuenton = 0.15
    descuento_cliente_frecuente = 0.10 + estudian_descuenton
    monto_descuento = precio * descuento_cliente_frecuente
    precio_final = precio - monto_descuento
else:
    monto_descuento = 0.0
    precio_final = precio

#resultado
print("\n--- Resumen ---")
print("Precio original:", precio)
print("Descuento aplicado:", monto_descuento)
print("Precio final:", precio_final)



