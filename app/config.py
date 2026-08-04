import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Agent App")
MODEL_NAME = os.getenv("MODEL_NAME", "default-model")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


def print_config():
    print("应用名称：", APP_NAME)
    print("模型名称：", MODEL_NAME)
    if OPENAI_API_KEY:
        print("API Key：已配置")
    else:
        print("API Key：未配置")
