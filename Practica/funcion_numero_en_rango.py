def numero_en_rango(valor, min, may):
    if min <= valor <= may:
        return True
    else:
        return False

print(numero_en_rango(12, 10, 12))
