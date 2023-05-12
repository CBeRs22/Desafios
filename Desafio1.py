import sqlite3

conx=sqlite3.connect("/CROSSANDINO.db") # Path del archivo.
dats=conx.cursor()
dats1=conx.cursor()
competidorxs=[]
for i in range(20):
    print(f"Ingrese los datos de la persona{i+1}")
    apelnomb=input("Apellido y Nombre: ")
    edad=int(input("Edad: "))
    if edad >= 18:
        mayor=edad
        mins=int(input("Minutos: "))
        segs=int(input("Segundos: "))
        tmpo=f"{mins:02d}:{segs:02d}"
        pais=input("País de origen: ")
        adultos=(apelnomb,mayor,tmpo,pais)
        dats.execute("INSERT INTO CategoriaAdultos VALUES (?, ?, ?, ?)",adultos)
    else:
        menor=edad
        mins=int(input("Minutos: "))
        segs=int(input("Segundos: "))
        tmpo=f"{mins:02d}:{segs:02d}"
        pais=input("País de origen: ")   
        menores=(apelnomb,menor,tmpo,pais)      
        dats1.execute("INSERT INTO CategoriaJuniors VALUES (?, ?, ?, ?)",menores)
competidorxs.append(adultos)
competidorxs.append(menores)
conx.commit()
conx.close()
print("Listo!")
