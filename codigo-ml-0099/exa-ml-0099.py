# Medina Anais NC 0099
import sys
import os
import pandas as pd

# Permitir importar dicc-0099.py desde la subcarpeta hermana
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos-de-entrada-ml-0099')))
import dicc_0099 # type: ignore

print("Anais Medina Machine Learning pandas, NC 0099")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Anais Medina Machine Learning pandas, NC 0099"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0099.datos_fabricas)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
import io
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Produccion diaria)
registrar("3. Estadísticas Generales de la Columna 'Produccion_diaria'", df['Produccion_diaria'].describe())

# 4. Ordenar Ascendente por Produccion diaria
df_asc_Produccion_diaria = df.sort_values(by="Produccion_diaria", ascending=True)
registrar("4. Ordenar Ascendente por Produccion_diaria", df_asc_Produccion_diaria)

# 5. Ordenar Descendente por Empleados
df_desc_Empleados = df.sort_values(by="Empleados", ascending=False)
registrar("5. Ordenar Descendente por Empleados", df_desc_Empleados)

# 7. Guardar el archivo resultados-ml-0099.md dentro de resultados-0099
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0099'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0099.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Anais Medina Machine Learning pandas, NC 0099")
print("Anais Medina NC 0099")