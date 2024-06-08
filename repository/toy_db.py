import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Postgres_toy:
    def __init__(self):
        self.data_base = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            database=os.getenv('DB_NAME'),
            password=os.getenv('DB_PASSWORD')
        )
        self.cursor = self.data_base.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS toys (
                    product_id SERIAL PRIMARY KEY,
                    toy_name VARCHAR(255),
                    toy_img VARCHAR(255),
                    toy_price VARCHAR(255),
                    toy_url VARCHAR(255)
                )
            """)

    def insert_into(self, *args):
        self.create_table()
        self.cursor.execute("""
                    INSERT INTO toys (toy_name, toy_img, toy_price, toy_url)
                    VALUES
                    (%s, %s, %s, %s)
                """, args)
        self.data_base.commit()

    def select_data(self):
        self.cursor.execute("""
            SELECT toy_name, toy_img, toy_price, toy_url
            FROM toys
        """)
        data = self.cursor.fetchall()
        return data
