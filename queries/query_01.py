def execute_query(spark):
    """
    Query 1: Total de crimes por tipo e por segmento das ruas do distrito de IGUATEMI durante o ano de 2016
    """
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
    
    print("\nExecutando Query 1...")
    return spark.sql(query)