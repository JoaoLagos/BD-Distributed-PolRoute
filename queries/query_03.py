def execute_query(spark):
    """
    Query 3: Total de ocorrências de Roubo de Celular e Roubo de Carro no bairro de SANTA EFIGÊNIA em 2015
    """
    query = """
    SELECT 
        SUM(c.total_armed_robbery_cellphone) AS robbery_cellphone,
        SUM(c.total_armed_robbery_auto) AS robbery_auto
    FROM crime c
    JOIN time t ON c.time_id = t.id
    JOIN segment s ON c.segment_id = s.id
    JOIN vertice v ON s.start_vertice_id = v.id OR s.final_vertice_id = v.id
    JOIN neighborhood n ON v.neighborhood_id = n.id
    WHERE n.name = 'Santa Efig�nia' AND t.year = 2015
    """
    
    print("\nExecutando Query 3...")
    return spark.sql(query)