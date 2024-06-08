# import psycopg2
#
# class Smartphone:
#     def __init__(self):
#         self.data_base = psycopg2.connect(
#             host='localhost',
#             user='postgres',
#             database='online_store',
#             password='123456'
#         )
#         self.cursor = self.data_base.cursor()
#
#     def create_table(self):
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS smartphone (
#                     product_id SERIAL PRIMARY KEY,
#                     smartphone_name VARCHAR(255),
#                     smartphone_img VARCHAR(255),
#                     smartphone_price VARCHAR(255),
#                     smartphone_url VARCHAR(255)
#                 )
#             """)
#     def insert_into(self, *args):
#         self.create_table()
#         self.cursor.execute(f"""
#                     INSERT INTO smartphone (smartphone_nam, smartphone_img, smartphone_price, smartphone_url)
#                     VALUES
#                     (%s, %s, %s, %s)
#                 """, args)
#         return self.data_base.commit()
#
#
#     def select_data(self):
#         self.cursor.execute("""
#             SELECT smartphone_name, smartphone_img, smartphone_price, smartphone_url
#             FROM smartphone
#         """)
#         data = self.cursor.fetchall()
#         return data
# Smartphone().select_data()
