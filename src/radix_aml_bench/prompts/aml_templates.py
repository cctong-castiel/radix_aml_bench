BASE_AML_POLICY = """
GLOBAL COMMERCIAL BANKING — AML / BSA & SANCTIONS COMPLIANCE MANUAL (REV 2026.4)
RULE AML-101 (Structuring / Smurfing): Multiple cash or wire transfers just below the $10,000 CTR threshold within a 5-business-day window from related entities require mandatory escalation.
RULE AML-102 (High-Risk Jurisdictions): Any cross-border wire involving FATF Grey/Black list jurisdictions, shell banks, or unverified offshore holding companies requires Enhanced Due Diligence (EDD) and HOLD_FOR_REVIEW.
RULE AML-103 (Rapid Movement / Layering): Funds credited and wired out (>85% of principal) within 24 hours with no clear commercial invoice trigger SAR review.
RULE AML-104 (Sanctions & PEP Screening): Any counterparty name fuzzy-matching OFAC SDN, EU Consolidated, or UN Sanctions lists—or senior Political Exposed Persons (PEPs) transacting above $50,000—requires immediate FREEZE_AND_ESCALATE.
RULE AML-105 (Trade-Based Money Laundering): Over/under-invoicing of dual-use goods, commodities, or electronics shipments inconsistent with customer KYC profile triggers HIGH risk.
"""

# Expand the shared context to simulate a realistic multi-page bank SOP (~2,800 tokens)
SHARED_SYSTEM_PROMPT = (
    "You are an automated Tier-2 Banking AML Compliance Auditor. "
    "Evaluate each wire transfer against the regulatory manual below and output ONLY valid JSON matching the schema.\n\n"
    + "\n".join([f"[Section {i}] {BASE_AML_POLICY}" for i in range(1, 18)])
)

# User prompt
user_prompt = "Audit this wire transfer (Request #{0}):\n{1}"
