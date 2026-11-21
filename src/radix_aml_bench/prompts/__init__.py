from radix_aml_bench.prompts.aml_templates import AML_SHARED_SYSTEM_PROMPT
from radix_aml_bench.prompts.aml_templates import user_prompt as AML_USER_PROMPT

SystemPromptRegistry = {
    "aml": AML_SHARED_SYSTEM_PROMPT
}

UserPromptRegistry = {
    "aml": AML_USER_PROMPT
}

__all__ = ["SystemPromptRegistry", "UserPromptRegistry"]