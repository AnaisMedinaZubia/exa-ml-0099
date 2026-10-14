# Reporte de Análisis de Datos - Pandas

`Anais Medina Machine Learning pandas, NC 0099`

## 1. DataFrame Convertido
```text
       Fabrica  Empleados  Produccion_diaria
0   Automotriz       2500                500
1    Alimentos       1800              10000
2       Textil       1200               2000
3  Electrónica       3000                800
4      Química        900                600
5  Metalúrgica       1500                400
```

## 2.1 Primeras Filas (head)
```text
      Fabrica  Empleados  Produccion_diaria
0  Automotriz       2500                500
1   Alimentos       1800              10000
```

## 2.2 Últimas Filas (tail)
```text
       Fabrica  Empleados  Produccion_diaria
4      Química        900                600
5  Metalúrgica       1500                400
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Fabrica                str
Empleados            int64
Produccion_diaria    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   Fabrica            6 non-null      str  
 1   Empleados          6 non-null      int64
 2   Produccion_diaria  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Produccion_diaria'
```text
count        6.000000
mean      2383.333333
std       3776.991748
min        400.000000
25%        525.000000
50%        700.000000
75%       1700.000000
max      10000.000000
Name: Produccion_diaria, dtype: float64
```

## 4. Ordenar Ascendente por Produccion_diaria
```text
       Fabrica  Empleados  Produccion_diaria
5  Metalúrgica       1500                400
0   Automotriz       2500                500
4      Química        900                600
3  Electrónica       3000                800
2       Textil       1200               2000
1    Alimentos       1800              10000
```

## 5. Ordenar Descendente por Empleados
```text
       Fabrica  Empleados  Produccion_diaria
3  Electrónica       3000                800
0   Automotriz       2500                500
1    Alimentos       1800              10000
5  Metalúrgica       1500                400
2       Textil       1200               2000
4      Química        900                600
```

`Anais Medina Machine Learning pandas, NC 0099`