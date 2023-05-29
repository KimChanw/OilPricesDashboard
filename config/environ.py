import os
import dotenv

env_file = dotenv.find_dotenv()
dotenv.load_dotenv(env_file)

class Environ:
    # 장고 시크릿 키
    SECRET_KEY = os.getenv('SECRET_KEY')

    # AWS 키
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    
    # snowflake 접속 정보
    ACCOUNT = os.getenv('ACCOUNT')
    PASSWORD = os.getenv('PASSWORD')
    USER = os.getenv('USER')

    DATABASE = os.getenv('DATABASE')
    SCHEMA = os.getenv('SCHEMA')