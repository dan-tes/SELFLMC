import os
from typing import final
import dotenv


@final
class VarEnv:
    dotenv.load_dotenv()
    DBUSER = os.environ.get("POSTGRES_USER")
    DBPASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DBHOST = os.environ.get("DBHOST")
    DBNAME = os.environ.get("POSTGRES_DB")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TESTER_API = os.environ.get("TESTER_API") == '1'
