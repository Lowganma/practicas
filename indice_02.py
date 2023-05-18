peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = round(peso / altura**2, 2)
print("Tu índice de masa corporal es", imc)
