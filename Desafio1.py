#Creación y conexion del archivo.db con sus dos respectetivas tablas.

import sqlite3

conx=sqlite3.connect("C:/User/LeonelCabral/CROSSANDINO.db") #Path del archivo.db
dats=conx.cursor()
dats1=conx.cursor()

tabmay='''
CREATE TABLE categoría_adultos(
    apellido_y_nombre TEXT,
    edad INTEGER,
    tiempo TEXT,
    pais_de_origen TEXT    
)
'''
tabmen='''
CREATE TABLE categoría_juniors(
    apellido_y_nombre TEXT,
    edad INTEGER,
    tiempo TEXT,
    pais_de_origen TEXT    
)
'''
dats.execute(tabmay)
dats1.execute(tabmen)

#Este es el proceso de ingresar los datos de todos los participantes.

competidorxs=[]
for i in range(20):
    print(f"\n #CATEGORÍA ADULTOS \n\n PARTICIPANTE N°{i+1}: ")
    apelnomb=input("Apellido y Nombre: ")    
    edad=int(input("Edad: "))
    
    while edad < 18:
        print("\n Por favor solo ingrese participantes mayores a 18 años, gracias \n")
        apelnomb=input("Apellido y Nombre: ")
        edad=int(input("Edad: "))
    mayor=edad
        
    mins=int(input("Minutos: "))
    segs=int(input("Segundos: "))
    tmpo=f"{mins:02d}:{segs:02d}"
    pais=input("País de origen: ")
    adultos=(apelnomb,mayor,tmpo,pais)
    dats.execute("INSERT INTO categoría_adultos VALUES (?, ?, ?, ?)",adultos)
    
competidorxs.append(adultos)
print("\n No hay mas cupos para la categoría Adultos. \n")

for h in range(20):
    print(f"\n #CATEGORÍA JUNIORS \n\n PARTICIPANTE N°{h+1}: ")
    apelnomb=input("Apellido y Nombre: ")
    
    edad=int(input("Edad: "))
    while edad > 17:
        print("\n Por favor solo ingrese participantes menores a 18 años, gracias \n")
        apelnomb=input("Apellido y Nombre: ")
        edad=int(input("Edad: "))
    menor=edad
        
    mins=int(input("Minutos: "))
    segs=int(input("Segundos: "))
    tmpo=f"{mins:02d}:{segs:02d}"
    pais=input("País de origen: ")   
    menores=(apelnomb,menor,tmpo,pais)      
    dats1.execute("INSERT INTO categoría_juniors VALUES (?, ?, ?, ?)",menores)
    
competidorxs.append(menores)

#Al terminar el bucle para los datos ingresados, se crea 2 consultas para cada tabla y generar los puestos del primero al último.

cons='''CREATE VIEW PuestosCatAdults AS SELECT RANK() OVER (ORDER BY Tiempo ASC) AS Puesto, *
FROM categoría_adultos
ORDER BY Tiempo ASC
'''
dats.execute(cons)

cons1='''CREATE VIEW PuestosCatJrs AS SELECT RANK() OVER (ORDER BY Tiempo ASC) AS Puesto, *
FROM categoría_juniors
ORDER BY Tiempo ASC
'''
dats1.execute(cons1)

#Finalizacion de la conexion del archivo.db con el archivo.py

conx.commit()
conx.close()
print("\n No hay mas cupos para la categoría Juniors. \n")
print("Datos ingresados exitosamente.")
