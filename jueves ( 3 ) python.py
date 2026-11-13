#Conversor de monedas con comisión
codigo = int(input("Código (1=EUR, 2=GBP, 3=JPY, 4=MXN): "))
monto = float(input("Monto en USD: "))
match codigo:
    case 1: tasa, comision = 0.92, 0.01
    case 2: tasa, comision = 0.78, 0.01
    case 3: tasa, comision = 149, 0.015
    case 4: tasa, comision = 17.2, 0.02
    case _: print("Código inválido"); exit()
resultado = monto * tasa * (1 - comision)
print(f"Resultado: {resultado:.2f} | Comisión: {monto * comision:.2f}")
