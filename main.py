import time
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast
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
    segment.createOrReplaceTempView("segment")

    
    broadcast(district).createOrReplaceTempView("district")
    broadcast(neighborhood).createOrReplaceTempView("neighborhood")
    broadcast(time).createOrReplaceTempView("time")
    broadcast(vertice).createOrReplaceTempView("vertice")

def main():
    # Criar sessão do Spark
    spark = SparkSession.builder \
        .appName("PolRoute-DS") \
        .config("spark.sql.repl.eagerEval.enabled", True) \
        .config("spark.hadoop.hadoop.security.authentication", "simple") \
        .config("spark.hadoop.hadoop.security.authorization", "false") \
        .config("spark.hadoop.io.native.lib.available", "false") \
        .getOrCreate()

    # Configurações de saída 
    SAVE_OUTPUT = True  # False para desativar salvamento
    OUTPUT_FORMAT = "csv" 
    
    # Criar pasta de resultados
    import os
    os.makedirs("results", exist_ok=True)

    # Carregar dados
    load_data(spark)

    # Lista de queries a serem executadas (essas queries são as que o professor pediu)
    queries = [
        lambda: query_01.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_02.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_03.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_04.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_05.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_06.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT),
        lambda: query_07.execute_query(spark, SAVE_OUTPUT, OUTPUT_FORMAT)
    ]

    # Executar queries e mostrar resultados
    for i, query in enumerate(queries, 1):
        start_time = time.time()
        resultado = query()
        resultado.show(truncate=False)
        end_time = time.time()
        print(f"Query {i} executada em {end_time - start_time:.2f} segundos.\n")

if __name__ == "__main__":
    main()
