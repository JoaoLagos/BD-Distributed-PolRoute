def execute_query(spark,  save_output=False, output_format="csv"):
    """
    Query 5: Total de roubos de carro e celular em todos os segmentos durante o ano de 2017
    """
    query = """
    SELECT 
        SUM(c.total_armed_robbery_cellphone) AS robbery_cellphone,
        SUM(c.total_armed_robbery_auto) AS robbery_auto
    FROM crime c
    JOIN time t ON c.time_id = t.id
    WHERE t.year = 2017
    """
    
    print("\nExecutando Query 5...")
    result = spark.sql(query)

    if save_output:
        output_path = f"results/query_05"
        if output_format == "csv":
            result.write.csv(output_path, header=True, mode="overwrite")
            print(f"Resultados salvos em {output_path}.csv")
        elif output_format == "parquet":
            result.write.parquet(output_path, mode="overwrite")
            print(f"Resultados salvos em {output_path}.parquet")
    
    return result