# Build sglang and vllm docker containers

## Steps to build the containers

```Shell
# Create a multi-arch builder once on macOS
docker buildx create --use --name amd64-builder

# Build and push SGLang image
docker buildx build --platform linux/amd64 \
  -f docker/Dockerfile.sglang \
  -t <YOUR_REGISTRY>/radix-aml-sglang:v1 \
  --push .

# Build and push vLLM image
docker buildx build --platform linux/amd64 \
  -f docker/Dockerfile.vllm \
  -t <YOUR_REGISTRY>/radix-aml-vllm:v1 \
  --push .
```
