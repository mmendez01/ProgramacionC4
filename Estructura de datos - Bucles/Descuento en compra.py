monto_compra = float(input("Ingresa el monto total de la compra: $"))

descuento_aplicado = 0.0
tasa_descuento = 0.0

if monto_compra > 1000:
    tasa_descuento = 0.15
elif monto_compra > 500:
    tasa_descuento = 0.10
elif monto_compra > 100:
    tasa_descuento = 0.05

if tasa_descuento > 0:
    descuento_aplicado = monto_compra * tasa_descuento
    total_final = monto_compra - descuento_aplicado
    print(f"\nMonto original: ${monto_compra:,.2f}")
    print(f"Descuento ({tasa_descuento*100:.0f}%): ${descuento_aplicado:,.2f}")
    print(f"Total a pagar: ${total_final:,.2f}")
else:
    print(f"\nNo aplica descuento.")
    print(f"Total a pagar: ${monto_compra:,.2f}")