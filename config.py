import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    def __init__(
        self,
        pg_user,
        pg_password,
        pg_port,
        pg_host,
        pg_name,
        aws_access_key_id,
        aws_secret_access_key,
        aws_endpoint_url,
        aws_bucket_name
    ):
        self.DB_PORT = pg_port
        self.DB_HOST = pg_host
        self.DB_NAME = pg_name
        self.DB_USER = pg_user
        self.DB_PASSWORD = pg_password
        self.AWS_ACCESS_KEY = aws_access_key_id
        self.AWS_SECRET_ACCESS_KEY = aws_secret_access_key
        self.AWS_ENDPOINT_URL = aws_endpoint_url
        self.AWS_BUCKET_NAME = aws_bucket_name

        # todo сделать 
        self.DATABASE_URL_ASYNC=f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_name}"
        self.DATABASE_URL_SYNC=f"postgresql+psycopg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_name}"

config = Config(
    pg_user=os.getenv("DB_USER"),
    pg_password=os.getenv("DB_PASSWORD"),
    pg_port=os.getenv("DB_PORT"),
    pg_host=os.getenv("DB_HOST"),
    pg_name=os.getenv("DB_NAME"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_endpoint_url=os.getenv("AWS_ENDPOINT_URL"),
    aws_bucket_name=os.getenv("AWS_BUCKET_NAME")
)