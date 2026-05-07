import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

_DEFAULT_DEV_KEY = "dev-only-change-me"


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", _DEFAULT_DEV_KEY)
    ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = ENV == "development"
    TESTING = False

    DUCKDB_PATH = os.environ.get(
        "DUCKDB_PATH", str(BASE_DIR / "data" / "omniconvert.duckdb")
    )

    VERSION = os.environ.get("OMNICONVERT_VERSION", "0.0.1")

    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

    ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")

    UMAMI_WEBSITE_ID = os.environ.get("UMAMI_WEBSITE_ID", "")
    UMAMI_SCRIPT_URL = os.environ.get("UMAMI_SCRIPT_URL", "")

    @classmethod
    def validate(cls, app_config: dict) -> None:
        env = app_config.get("ENV", "production")
        if env != "development" and not app_config.get("TESTING"):
            if app_config["SECRET_KEY"] == _DEFAULT_DEV_KEY:
                sys.exit(
                    "FATAL: SECRET_KEY is the development default while "
                    "FLASK_ENV != 'development'. Set SECRET_KEY in .env."
                )
