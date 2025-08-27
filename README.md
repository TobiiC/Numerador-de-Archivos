#📂 File Enumerator

Este script en Python permite renombrar todos los archivos dentro de una carpeta, asignándoles un nombre ordenado con un prefijo definido (por defecto archivo_1, archivo_2, …).

Es útil para organizar imágenes, documentos o cualquier tipo de archivo que quieras tener enumerado de forma secuencial.

#🚀 Características

Renombra automáticamente todos los archivos de una carpeta.

Conserva la extensión original (.jpg, .png, .pdf, etc.).

Simple y rápido de ejecutar.

#📋 Requisitos

Python 3 instalado en tu sistema.

No requiere librerías externas, solo se usa la librería estándar (os).

#🔧 Uso

Clonar o descargar este repositorio.

Editar la variable carpeta en el archivo enumerador.py con la ruta de la carpeta que quieras procesar:

carpeta = "C:/Users/TuUsuario/Downloads/Fotos"


Ejecutar el script dentro de la carpeta program:

numerador_archivos.py


Todos los archivos en la carpeta serán renombrados con el formato:

archivo_1.extension
archivo_2.extension
archivo_3.extension
...

#⚠️ Notas

Haz una copia de seguridad antes de ejecutar el script, ya que los nombres originales se sobrescriben.

El orden de renombrado depende de cómo el sistema devuelve la lista de archivos.

#🛠️ Mejoras futuras

Opción de personalizar el prefijo (foto_, archivo_, documento_, etc.).

Ordenar archivos por fecha de creación/modificación antes de renombrar.

Interfaz gráfica básica para elegir carpeta y prefijo.