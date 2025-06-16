def execute_query(spark):
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
    return spark.sql(query)