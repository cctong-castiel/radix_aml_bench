import asyncio
import logging

from radix_aml_bench.core import Engine
from radix_aml_bench.settings import SGLANG_URL, VLLM_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    sglang_engine = Engine(name="SGLang (RadixAttention)", url=SGLANG_URL)
    vllm_engine = Engine(name="vLLM (Baseline)", url=VLLM_URL)

    # run the engine main method
    sglang_results = await sglang_engine.run_benchmark(domain_name="aml")
    vllm_results = await vllm_engine.run_benchmark(domain_name="aml")

    # show results
    logger.info("SGLang and vLLM results comparison")
    text_format = "{:<24} | {:<18} | {:<18}"
    logger.info(text_format.format("Metric", sglang_results.engine, vllm_results.engine))
    logger.info("-" * 60)
    for key in list(sglang_results.model_json_schema().keys()):
        logger.info(
            text_format.format(key, str(sglang_results[key]), str(vllm_results[key]))
        )


if __name__ == "__main__":
    asyncio.run(main)