import asyncio
import logging

from radix_aml_bench.core import Engine
from radix_aml_bench.settings import SGLANG_API_KEY, SGLANG_URL, VLLM_API_KEY, VLLM_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    sglang_engine = Engine(name="SGLang (RadixAttention)", url=SGLANG_URL, api_key=SGLANG_API_KEY)
    vllm_engine = Engine(name="vLLM (Baseline)", url=VLLM_URL, api_key=VLLM_API_KEY)

    # run the engine main method
    sglang_results = await sglang_engine.run_benchmark(domain_name="aml")
    vllm_results = await vllm_engine.run_benchmark(domain_name="aml")

    # show results
    logger.info("SGLang and vLLM results comparison")
    text_format = "{:<24} | {:<24} | {:<24}"
    logger.info(text_format.format("Metric", sglang_results.engine, vllm_results.engine))
    logger.info("-" * 78)
    sglang_data = sglang_results.model_dump()
    vllm_data = vllm_results.model_dump()
    for key in vllm_data:
        logger.info(
            text_format.format(key, str(sglang_data[key]), str(vllm_data[key]))
        )


if __name__ == "__main__":
    asyncio.run(main())