
from typing import Literal

from pydantic import BaseModel, Field


class AMLAuditResult(BaseModel):
    transaction_id: str
    risk_level: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    triggered_rules: list[str] = Field(
        description="List of specific AML/BSA rule codes violated, e.g., AML-104"
    )
    requires_sar_filing: bool = Field(
        description="Whether a Suspicious Activity Report (SAR) must be filed within 30 days"
    )
    sanctions_hit: bool
    recommended_action: Literal["APPROVE", "HOLD_FOR_REVIEW", "FREEZE_AND_ESCALATE"]
    audit_rationale: str = Field(description="Concise 1-sentence compliance justification")


# Sample synthetic wire-transfer payloads
SAMPLE_TRANSACTIONS = [
    "TXN-90811 | Sender: Apex Global Trading Ltd (Cayman Islands) | Beneficiary: Eastern Star Logistics (Hong Kong) | Amount: $485,000 USD | Memo: Industrial valves shipment #441 | Notes: Account opened 12 days ago; funds arrived from 4 shell entities 3 hours prior.",
    "TXN-90812 | Sender: Thames Valley Manufacturing PLC (UK) | Beneficiary: Rheinmetall Components GmbH (Germany) | Amount: $62,400 EUR | Memo: Invoice 2026-889 CNC machine parts | Notes: Established 9-year corporate client, recurring monthly supplier payment.",
    "TXN-90813 | Sender: Horizon Ventures LLC (Delaware) | Beneficiary: Pacific Rim Consulting (Singapore) | Amount: $9,850 USD | Memo: Advisory fee tranche 4 | Notes: 4th transfer of $9,800-$9,950 sent over the past 4 days to the same beneficiary.",
    "TXN-90814 | Sender: Viktor Petrov Holdings (Cyprus) | Beneficiary: Al-Noor Precious Metals DMCC (UAE) | Amount: $1,250,000 USD | Memo: Gold bullion settlement | Notes: Beneficial owner flagged as close associate of sanctioned state-owned enterprise executive.",
]