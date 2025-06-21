def execute_query(spark, save_output=False, output_format="csv"):
    """
    Query 3 : Total de roubos de celular e carro no bairro SANTA EFIGÊNIA em 2015
    """
    query = """
    WITH santa_vertices AS (
        SELECT v.id
        FROM vertice v
        JOIN neighborhood n ON v.neighborhood_id = n.id
        WHERE n.name = 'Santa Efig�nia'
    ),
    santa_segments AS (
        SELECT s.id AS segment_id
        FROM segment s
        JOIN santa_vertices v1 ON s.start_vertice_id = v1.id
        UNION ALL
        SELECT s.id AS segment_id
        FROM segment s
        JOIN santa_vertices v2 ON s.final_vertice_id = v2.id
    )
    SELECT 
        SUM(c.total_armed_robbery_cellphone) AS robbery_cellphone,
        SUM(c.total_armed_robbery_auto) AS robbery_auto
    FROM crime c
    JOIN time t ON c.time_id = t.id
    JOIN santa_segments s ON c.segment_id = s.segment_id
    WHERE t.year = 2015
    """
    print("\nExecutando Query 3 (corrigida)...")
    result = spark.sql(query)

    if save_output:
        result.write.format(output_format).option("header", True).mode("overwrite").save("results/query_03")
        print("Resultados salvos em results/query_03")

    return result
