import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

def get_connection():
    db_url = os.getenv('JAWSDB_URL')
    parsed = urlparse(db_url)

    return pymysql.connect(
        host=parsed.hostname,
        user=parsed.username,
        password=parsed.password,
        database=parsed.path.lstrip('/'),
        port=parsed.port or 3306,
        cursorclass=pymysql.cursors.DictCursor
    )
