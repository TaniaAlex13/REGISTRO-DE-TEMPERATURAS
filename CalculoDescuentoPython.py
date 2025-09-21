# Programa para calcular el descuento

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.
    :para monto_total: float -> Monto total de la compra
    :para porcentaje_descuento: float -> Porcentaje de descuento (por defecto 10%)
    :return: float -> Monto del descuento calculado
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal

if __name__ == "__main__":
    # Llamada 1: solo monto (usa descuento por defecto del 10%)
    monto1 = 200.0
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra: ${monto1:.2f} | Descuento aplicado (10%): ${descuento1:.2f} | Monto final: ${monto_final1:.2f}")

    # Llamada 2: monto + porcentaje de descuento personalizado

    monto2 = 350.0
    porcentaje2 = 25
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    print(f"Compra: ${monto2:.2f} | Descuento aplicado ({porcentaje2}%): ${descuento2:.2f} | Monto final: ${monto_final2:.2f}")
