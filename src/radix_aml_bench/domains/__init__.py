from radix_aml_bench.domains.aml_domain import SAMPLE_TRANSACTIONS, AMLAuditResult

ResponseRegistry = {
    "aml": AMLAuditResult
}

SampleRegistry = {
    "aml": SAMPLE_TRANSACTIONS
}

__all__ = ["ResponseRegistry", "SampleRegistry"]