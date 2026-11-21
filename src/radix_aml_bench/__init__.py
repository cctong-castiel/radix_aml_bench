import asyncio


def main() -> None:
    from radix_aml_bench.main import main as _async_main

    asyncio.run(_async_main())
