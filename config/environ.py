import os
from dotenv import load_dotenv

load_dotenv()


class Environ:

    # 장고 시크릿 키
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # AWS 키
    AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.environ.get("AWS_REGION")