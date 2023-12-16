import os
from sqlalchemy import create_engine, MetaData, Engine
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": int(os.environ.get("POSTGRES_PORT")),
}

connection_string: str = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"

engine: Engine = create_engine(connection_string)
metadata: MetaData = MetaData()

metadata.bind = engine
