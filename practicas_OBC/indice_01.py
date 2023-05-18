### practica openBootcamp ###
print("introduce tu peso en kg:")
peso = float(input())
print("introduce tu estatura en Metros:")
altura = float(input())
masa = round(peso / altura**2, 2)
print("tu masa es:", masa)
