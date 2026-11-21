import os

from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = "API_KEY"
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-7B-Instruct")
SGLANG_URL = os.getenv("SGLANG_BASE_URL", "http://localhost:30000/v1")
VLLM_URL = os.getenv("VLLM_BASE_URL", "http://localhost:8000/v1")

CONCURRENCY = int(os.getenv("CONCURRENCY", "32"))
TOTAL_REQUESTS = int(os.getenv("TOTAL_REQUESTS", "128"))
MAX_TOKENS = 256