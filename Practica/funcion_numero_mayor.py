def numero_mayor(primero, segundo, tercero):
    numero_grande = primero
    if numero_grande < segundo:
        numero_grande = segundo
    if numero_grande < tercero:
        numero_grande = tercero
    return numero_grande

print(numero_mayor(88, 77, 99 * 2))
