#Creación y conexion del archivo.db con sus dos respectetivas tablas.

import sqlite3

conx=sqlite3.connect("C:/Users/LeonelCabral/Desafio1/CROSSANDINO.db")
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
    print(f"Categoría Adultos: PARTICIPANTE N°{i+1}: ")
    apelnomb=input("Apellido y Nombre: ")    
    edad=int(input("Edad: "))
    
    while edad < 18:
        print("Por favor solo ingrese participantes mayores a 18 años, gracias")
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
print("No hay mas cupos para la categoría Adultos")

for h in range(20):
    print(f"Categoría Juniors: PARTICIPANTE N°{h+1}: ")
    apelnomb=input("Apellido y Nombre: ")
    
    edad=int(input("Edad: "))
    while edad > 17:
        print("Por favor solo ingrese participantes menores a 18 años, gracias")
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

#Al terminar el bucle para los datos ingresados, finalizamos la conexion del archivo.db y el archivo.py

conx.commit()
conx.close()
print("No hay mas cupos para la categoría Juniors.")
print("vuelvas prontos!!!")
