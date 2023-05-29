import os
import snowflake.connector
from config.environ import Environ

class SnowflakeSession:
    @classmethod
    def snowflake_connector(cls):
        conn = snowflake.connector.connect(
            account=Environ.ACCOUNT,
            user=Environ.USER,
            password=Environ.PASSWORD,
            autocommit=True,
            database=Environ.DATABASE,
            schema=Environ.SCHEMA
        )
        
        cursor = conn.cursor()
        return cursor