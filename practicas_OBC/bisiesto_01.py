def es_bisiesto(año):
    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False


año = int(input("introduce un año: "))

if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto")
