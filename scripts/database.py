# database.py
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Function to save a smartphone record to PostgreSQL
def save_to_postgres(smartphones, postgres_conn_id='db_conn_jakub'):
    pg_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
    
    for smartphone in smartphones:
        insert_query = """
        INSERT INTO smartphones (name, price, guarantee, operating_system, communication, battery,
                                 processor, ram, capacity, display, display_diagonal, display_resolution,
                                 display_refresh_rate, front_cam_resolution, back_cam_resolution, wireless_charging, url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (url) DO NOTHING;  -- Avoid duplicate entries
        """
        pg_hook.run(insert_query, parameters=(
            smartphone['name'], smartphone['price'], smartphone['guarantee'], smartphone['operating_system'],
            smartphone['communication'], smartphone['battery'], smartphone['processor'], smartphone['ram'],
            smartphone['capacity'], smartphone['display'], smartphone['display_diagonal'],
            smartphone['display_resolution'], smartphone['display_refresh_rate'],
            smartphone['front_cam_resolution'], smartphone['back_cam_resolution'],
            smartphone['wireless_charging'], smartphone['url']
        ))
        
print("Database functions created")