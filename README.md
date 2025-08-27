# 📂 File Enumerator

Este script en **Python** permite renombrar todos los archivos dentro de una carpeta, asignándoles un nombre ordenado con un prefijo definido (por defecto `archivo_1`, `archivo_2`, …).

Es útil para organizar imágenes, documentos o cualquier tipo de archivo que quieras tener enumerado de forma secuencial.

---

## 🚀 Características
- Renombra automáticamente todos los archivos de una carpeta.  
- Conserva la extensión original (`.jpg`, `.png`, `.pdf`, etc.).  
- Simple y rápido de ejecutar.  

---

## 📋 Requisitos
- Python 3 instalado en tu sistema.  
- No requiere librerías externas, solo se usa la librería estándar (`os`).  

---

## 🔧 Uso
1. Clonar o descargar este repositorio.  
2. Editar la variable `carpeta` en el archivo `enumerador.py` con la ruta de la carpeta que quieras procesar:  

   ```python
   carpeta = "C:/Users/TuUsuario/Downloads/Fotos"

## ⚠️ Notas 
Haz una copia de seguridad antes de ejecutar el script, ya que los nombres originales se sobrescriben.

El orden de renombrado depende de cómo el sistema devuelve la lista de archivos.