# vLLM and SGLang use cases

## Similarity between them

1. Both vLLM and SGLang solves the same problem - Reduce the waste of GPU memories for KV cache since a maximum sequence length of GPU memories are pre-allocated for GPU processing

## Difference between them

### vLLM

1. Instead of one contiguous KV cache block per request, it is split into fixed-size pages, 16 tokens each.
2. A block table maps each request logical positions to physical pages wherever the are free in GPU memory.
3. Non-continguous, no pre-allocation, pages are immediately freed when a request finishes.
4. vLLM can serve more concurrent requests on the same GPU.

### SGLang

1. It is different approach from vLLM. It asks why are we computing the same KV cache entries for the same tokens over and over across every request?
2. It eliminates repetitive full prefill operations to GPU which waste GPU cycles.
3. It organizes KV cache as Radix tree. The system prompt lives at the root, computed exactly once. Every new requests share the same instant cache hit with not re-process again and only process the new tokens and saved in the Radix tree.
4. The tree handles complex sharing, agent contexts, multi-turn conversations, shared chain of thought prefixes all benefits from the tree.
5. It reduces higher throughput and faster first time to token.

### Structured output, JSON schemas, function calling, grammar constrained generation

1. vLLM handles through logit masking. Grammar engine inspects the partial outputs in every decoding step to predict valid next tokens and filter vocabulary before sampling. Thus it runs on every single token in python. Eg. vocabulary has 32000 tokens, it checks all of them before generate a next token.
2. SGLang will compile the JSON schema into the finite state machine(FSM) at the start. No per-token python overhead. Constrained decoding becomes nearly free.

## Tensor Parallelism & Pipeline Parallelism

| Feature                  | vLLM                      | SGLang            |
| ------------------------ | ------------------------- | ----------------- |
| Tensor parallelism       | supported - more matrue   | supported         |
| Pipeline parallelism     | supported - multi-node    | supported         |
| Expert paralleslism(MoE) | supported - Deepseek, etc | supported         |
| Production maturity      | More mature               | Less mature<br /> |

## Reference

1. Explain vLLM and SGLang usage: [www.youtube.com/watch?v=18AkpuX3vkY](https://www.youtube.com/watch?v=18AkpuX3vkY)
2. Parallelism optimization: [www.youtube.com/watch?v=DdmgD5RMe1U](https://www.youtube.com/watch?v=DdmgD5RMe1U)
