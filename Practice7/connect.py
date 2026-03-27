import psycopg2
from config import load_config

def connect(config):
    try:
        conn = psycopg2.connect(**config)
        print("Connected to PostgreSQL!")
        return conn   # 🔥 ВОТ ЭТО ГЛАВНОЕ
    except Exception as error:
        print(error)