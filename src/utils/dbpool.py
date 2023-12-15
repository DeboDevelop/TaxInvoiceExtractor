import os
from sqlalchemy import create_engine, pool
from dotenv import load_dotenv
from utils.logger import logger


class ConnectionPool:
    def __init__(self, minconn, maxconn, **kwargs):
        # Store database connection parameters
        self._db_params = kwargs

        # Create a SQLAlchemy connection pool
        self._pool = pool.QueuePool(
            creator=self._create_connection,
            pool_size=minconn,
            max_overflow=maxconn,
        )
        logger.info("Connection pool created.")

    def _create_connection(self):
        # Custom connection creator function
        connection_string = self._build_connection_string()
        return create_engine(connection_string).connect()

    def _build_connection_string(self):
        # Build the PostgreSQL connection string
        return f"postgresql+psycopg2://{self._db_params['user']}:{self._db_params['password']}@{self._db_params['host']}:{self._db_params['port']}/{self._db_params['dbname']}"

    def get_connection(self):
        # Get a connection from the pool
        return self._pool.connect()

    def close_all_connections(self):
        # Close all connections in the pool
        self._pool.dispose()


load_dotenv()
DB_CONFIG = {
    "dbname": os.environ.get("POSTGRES_DB"),
    "user": os.environ.get("POSTGRES_USER"),
    "password": os.environ.get("POSTGRES_PASSWORD"),
    "host": os.environ.get("POSTGRES_HOST"),
    "port": int(os.environ.get("POSTGRES_PORT")),
}

connection_pool = ConnectionPool(minconn=1, maxconn=10, **DB_CONFIG)
