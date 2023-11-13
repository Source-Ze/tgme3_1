import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 26484720))

    API_HASH = os.environ.get("API_HASH", "361cfa5b07e7cef672ecd44c0f4e17cb")

    