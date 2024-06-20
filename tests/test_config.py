from dotenv import dotenv_values

config = dotenv_values(".env")

test_config = {"DB_URI": config["DB_URI"], "DB_NAME": config["DB_NAME"]}
