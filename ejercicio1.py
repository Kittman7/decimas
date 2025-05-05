#Nombre y contraseña

nombre = "luis"
Contraseña = "777"

nombre = input(" Ingrese su nombre ")
Contraseña = input ("ingrese su contraseña ")

if nombre == "luis" and Contraseña == "777":
    print("contraseña correcta") 
elif nombre == "luis" and Contraseña != "777": 
    print("tu contraseña empieza con: " + Contraseña[0]) 
else:
    print("tu nombre y contraseña son incorrectos")