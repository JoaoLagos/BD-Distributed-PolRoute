def execute_query(spark):
    """
    Query 1: Total de crimes por tipo e por segmento das ruas do distrito de IGUATEMI durante o ano de 2016
    """
    query = """
    SELECT 
    d.name AS distrito,
    n.name AS bairro,
    COUNT(s.id) AS total_segmentos
    FROM segment s
    JOIN vertice v ON s.start_vertice_id = v.id
    JOIN district d ON v.district_id = d.id
    JOIN neighborhood n ON v.neighborhood_id = n.id
    GROUP BY d.name, n.name
    ORDER BY total_segmentos DESC
    """

    print("\nExecutando Query 2...")
    return spark.sql(query)