def execute_query(spark,  save_output=False, output_format="csv"):
    """
    Query 6: IDs dos segmentos com maior índice criminal (soma total de crimes) em Novembro de 2010
    """
    query = """
    SELECT 
        c.segment_id,
        SUM(
            c.total_feminicide + c.total_homicide + c.total_felony_murder + 
            c.total_bodily_harm + c.total_theft_cellphone + c.total_armed_robbery_cellphone + 
            c.total_theft_auto + c.total_armed_robbery_auto
        ) AS total_crimes
    FROM crime c
    JOIN time t ON c.time_id = t.id
    WHERE t.year = 2010 AND t.month = 11
    GROUP BY c.segment_id
    ORDER BY total_crimes DESC
    LIMIT 10
    """
    
    print("\nExecutando Query 6...")
    result = spark.sql(query)

    if save_output:
        output_path = f"results/query_06"
        if output_format == "csv":
            result.write.csv(output_path, header=True, mode="overwrite")
            print(f"Resultados salvos em {output_path}.csv")
        elif output_format == "parquet":
            result.write.parquet(output_path, mode="overwrite")
            print(f"Resultados salvos em {output_path}.parquet")
    
    return result