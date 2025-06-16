import findspark
findspark.init()

from pyspark.sql import SparkSession

# Criar sessão do Spark
spark = SparkSession.builder \
    .appName("PolRoute-DS") \
    .config("spark.sql.repl.eagerEval.enabled", True) \
    .getOrCreate()

# Carregar os CSVs
crime = spark.read.csv("csv_databases/crime.csv", header=True, sep=";", inferSchema=True)
district = spark.read.csv("csv_databases/district.csv", header=True, sep=";", inferSchema=True)
neighborhood = spark.read.csv("csv_databases/neighborhood.csv", header=True, sep=";", inferSchema=True)
segment = spark.read.csv("csv_databases/segment.csv", header=True, sep=";", inferSchema=True)
time = spark.read.csv("csv_databases/time.csv", header=True, sep=";", inferSchema=True)
vertice = spark.read.csv("csv_databases/vertice.csv", header=True, sep=";", inferSchema=True)

# Criar views temporárias
crime.createOrReplaceTempView("crime")
district.createOrReplaceTempView("district")
neighborhood.createOrReplaceTempView("neighborhood")
segment.createOrReplaceTempView("segment")
time.createOrReplaceTempView("time")
vertice.createOrReplaceTempView("vertice")

# Consulta SQL completa
query = """
SELECT 
  c.segment_id,
  SUM(c.total_feminicide) AS feminicide,
  SUM(c.total_homicide) AS homicide,
  SUM(c.total_felony_murder) AS felony_murder,
  SUM(c.total_bodily_harm) AS bodily_harm,
  SUM(c.total_theft_cellphone) AS theft_cellphone,
  SUM(c.total_armed_robbery_cellphone) AS robbery_cellphone,
  SUM(c.total_theft_auto) AS theft_auto,
  SUM(c.total_armed_robbery_auto) AS robbery_auto
FROM crime c
JOIN time t ON c.time_id = t.id
JOIN segment s ON c.segment_id = s.id
JOIN vertice v ON s.start_vertice_id = v.id OR s.final_vertice_id = v.id
JOIN district d ON v.district_id = d.id
WHERE d.name = 'IGUATEMI' AND t.year = 2016
GROUP BY c.segment_id
ORDER BY c.segment_id
"""

resultado = spark.sql(query)
resultado.show(truncate=False)


