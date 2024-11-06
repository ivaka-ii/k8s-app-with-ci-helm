from flask import Flask
import os
from sqlalchemy import create_engine

app = Flask(__name__)

# Database environment configuration
DB_USER = os.environ.get('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
DB_HOST = os.environ.get('POSTGRES_HOST', 'postgresql')
DB_NAME = os.environ.get('POSTGRES_DB', 'postgres')

# URL for the database
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

@app.route('/')
def hello_world():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute("SELECT version();")
            version = result.fetchone()[0]
        return f'Hello, World! Connected to PostgreSQL: {version}'
    except Exception as e:
        return f'Error connecting to database: {str(e)}'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)