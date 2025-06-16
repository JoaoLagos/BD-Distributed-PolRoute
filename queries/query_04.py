def execute_query(spark):
    """
    Query 4: Total de crimes por tipo em vias de mão única da cidade durante o ano de 2012
    """
    query = """
    SELECT 
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
    WHERE t.year = 2012 AND LOWER(s.oneway) = 'yes'
    """
    
    print("\nExecutando Query 4...")
    return spark.sql(query)
