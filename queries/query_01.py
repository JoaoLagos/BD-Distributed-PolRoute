def execute_query(spark, save_output=False, output_format="csv"):
    """
    Query 1 : Total de crimes por tipo e por segmento no distrito IGUATEMI durante 2016.
    """
    query = """
    WITH iguatemi_vertices AS (
        SELECT v.id
        FROM vertice v
        JOIN district d ON v.district_id = d.id
        WHERE d.name = 'IGUATEMI'
    ),
    iguatemi_segments AS (
        SELECT s.id AS segment_id
        FROM segment s
        JOIN iguatemi_vertices v1 ON s.start_vertice_id = v1.id
        UNION ALL
        SELECT s.id AS segment_id
        FROM segment s
        JOIN iguatemi_vertices v2 ON s.final_vertice_id = v2.id
    )
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
    JOIN iguatemi_segments s ON c.segment_id = s.segment_id
    WHERE t.year = 2016
    GROUP BY c.segment_id
    ORDER BY c.segment_id
    """

    print("\nExecutando Query 1 (corrigida)...")
    result = spark.sql(query)

    if save_output:
        output_path = "results/query_01"
        result.write.format(output_format).option("header", True).mode("overwrite").save(output_path)
        print(f"Resultados salvos em {output_path} ({output_format})")

    return result
