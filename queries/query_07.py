def execute_query(spark):
    """
    Query 7: IDs dos segmentos com maior índice criminal durante finais de semana de 2018
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
    WHERE t.year = 2018 AND (t.weekday = 'saturday' OR t.weekday = 'sunday')
    GROUP BY c.segment_id
    ORDER BY total_crimes DESC
    LIMIT 10
    """
    
    print("\nExecutando Query 7...")
    return spark.sql(query)