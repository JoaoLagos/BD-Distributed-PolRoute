import time
import findspark
findspark.init()

from pyspark.sql import SparkSession
from queries import query_01, query_02, query_03, query_04, query_05, query_06, query_07

def load_data(spark):
    """Carrega todos os arquivos CSV"""

    crime = spark.read.csv("csv_databases/crime.csv", header=True, sep=";", inferSchema=True)
    district = spark.read.csv("csv_databases/district.csv", header=True, sep=";", inferSchema=True)
    neighborhood = spark.read.csv("csv_databases/neighborhood.csv", header=True, sep=";", inferSchema=True)
    segment = spark.read.csv("csv_databases/segment.csv", header=True, sep=";", inferSchema=True)
    time = spark.read.csv("csv_databases/time.csv", header=True, sep=";", inferSchema=True)
    vertice = spark.read.csv("csv_databases/vertice.csv", header=True, sep=";", inferSchema=True)

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

    # Lista de queries a serem executadas (essas queries são as que o professor pediu)
    queries = [
        query_01.execute_query,
        query_02.execute_query,
        query_03.execute_query,
        query_04.execute_query,
        query_05.execute_query,
        query_06.execute_query,
        query_07.execute_query
    ]

    # Executar queries e mostrar resultados
    for i, query in enumerate(queries, 1):
        start_time = time.time()
        resultado = query(spark)
        resultado.show(truncate=False)
        end_time = time.time()
        print(f"Query {i} executada em {end_time - start_time:.2f} segundos.\n")

if __name__ == "__main__":
    main()
