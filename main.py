import findspark
findspark.init()

from pyspark.sql import SparkSession
from queries import query_01, query_02, query_03, query_04, query_05

def load_data(spark):
    """Carrega todos os arquivos CSV"""
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

def main():
    # Criar sessão do Spark
    spark = SparkSession.builder \
        .appName("PolRoute-DS") \
        .config("spark.sql.repl.eagerEval.enabled", True) \
        .getOrCreate()

    # Carregar dados
    load_data(spark)

    # Executar cada query
    queries = [
        query_01.execute_query,
        query_02.execute_query
    ]

    # Executar queries e mostrar resultados
    for query in queries:
        resultado = query(spark)
        resultado.show(truncate=False)

if __name__ == "__main__":
    main()