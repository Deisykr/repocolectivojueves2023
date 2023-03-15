#controlador=5

#while controlador<10:
   # print("estoy saltando")
    #controlador=controlador+1

controlador=100    

print ("***** EMAPANADAS EL MACHETICO")
print("1. Agregar un sabor de empanada")
print("2. Ver el sabro de empanada registrado")
print("3. SALIR")

while controlador!=3:
    controlador=int(input("Digita una opción:  "))
    if(controlador==1):
        sabor=input("que sabor de empanda desea:")
        print("Elegiste opción 1")
    elif(controlador==2):
        print(f"El sabor es {sabor}")
        print("elegiste la opción 2")
    elif(controlador ==3):
        print("Hasta luego")
    else:
        print("elige una opción valida")
        
    