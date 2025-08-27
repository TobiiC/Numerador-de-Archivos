import os

carpeta = "Tu ruta/aqui"
archivos = os.listdir(carpeta)

for i, archivo in enumerate(archivos, start=1):
    extension = archivo.split(".")[-1]
    nuevo_nombre = f"Archivo_{i}.{extension}"
    ruta_vieja = os.path.join(carpeta, archivo)
    ruta_nueva = os.path.join(carpeta, nuevo_nombre)
    os.rename(ruta_vieja, ruta_nueva)

print("Renombrado completo ✅")