BASE_AML_POLICY = """
Anti-Money Laundary rules:
RULE AML-101 (Structuring / Smurfing): Multiple cash transactions just below the $10,000 Currency Transaction Report (CTR) threshold within a 5-business-day rolling window by or on behalf of related entities—or split wire transfers designed to evade recordkeeping or internal controls—require mandatory Suspicious Activity Report (SAR) escalation.
RULE AML-102 (High-Risk Jurisdictions): Any cross-border wire involving FATF High-Risk (Black List) or Increased Monitoring (Grey List) jurisdictions, or unverified offshore holding companies, requires Enhanced Due Diligence (EDD) and HOLD_FOR_REVIEW; transactions involving foreign shell banks are strictly prohibited and must be rejected.
RULE AML-103 (Rapid Movement / Layering): Funds credited and wired out (>85% of principal) within 24 hours without an apparent lawful business purpose or supporting commercial invoice trigger a mandatory SAR investigation (for suspicious activity totaling $5,000 or more).
RULE AML-104 (Sanctions & PEP Screening): Any counterparty name matching OFAC SDN, EU Consolidated, or UN Sanctions lists requires HOLD_FOR_REVIEW to clear false positives, followed by immediate FREEZE_AND_ESCALATE (blocking) upon confirmation; non-sanctioned senior Politically Exposed Persons (PEPs) transacting above $50,000 require HOLD_FOR_REVIEW, Enhanced Due Diligence (EDD), and senior management approval.
RULE AML-105 (Trade-Based Money Laundering): Apparent over- or under-invoicing, phantom shipments, or the movement of dual-use goods, high-value commodities, or electronics inconsistent with the customer's established KYC business profile triggers a HIGH risk rating, trade-document audit, and SAR/proliferation-financing review.
"""

# Expand the shared context to simulate a realistic multi-page bank SOP (~10,500 tokens)
SHARED_SYSTEM_PROMPT = (
    "You are an automated Tier-2 Banking AML Compliance Auditor. "
    "Evaluate each wire transfer against the regulatory manual below and output ONLY valid JSON matching the schema.\n\n"
    + "\n".join([f"[Section {i}] {BASE_AML_POLICY}" for i in range(1, 51)])
)

# User prompt (place the variable request ID at the end to maximize prefix sharing)
user_prompt = "Audit this wire transfer:\n{1}\n[Audit Reference #{0}]"
