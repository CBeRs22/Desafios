import sqlite3

conx=sqlite3.connect("CROSSANDINO.db") # Path del archivo.
dats=conx.cursor()
competidorxs=[]
for i in range(2):
    print(f"Ingrese los datos de la persona{i+1}")
    apelnomb=input("Apellido y Nombre: ")
    psto=(i+1)
    edad=int(input("Edad: "))
    mins=int(input("Minutos: "))
    segs=int(input("Segundos: "))
    tmpo=f"{mins:02d}:{segs:02d}"
    pais=input("País de origen: " )
    compe=(psto,apelnomb,edad,tmpo,pais)
    dats.execute("INSERT INTO Categorias VALUES (?, ?, ?, ?, ?)", compe)
competidorxs.append(compe)
conx.commit()
conx.close()
print("Listo!")
