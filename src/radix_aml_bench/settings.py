import os

from dotenv import load_dotenv

load_dotenv(override=True)

VLLM_API_KEY = os.getenv("VLLM_API_KEY") or "VLLM_API_KEY"
SGLANG_API_KEY = os.getenv("SGLANG_API_KEY") or "SGLANG_API_KEY"
MODEL_NAME = os.getenv("MODEL_NAME") or "Qwen/Qwen2.5-7B-Instruct"
SGLANG_URL = os.getenv("SGLANG_BASE_URL") or "http://localhost:30000/v1"
VLLM_URL = os.getenv("VLLM_BASE_URL") or "http://localhost:8000/v1"

print(f"VLLM_URL: {VLLM_URL}")
print(f"SGLANG_URL: {SGLANG_URL}")

CONCURRENCY = int(os.getenv("CONCURRENCY") or "32")
TOTAL_REQUESTS = int(os.getenv("TOTAL_REQUESTS") or "128")
MAX_TOKENS = 256