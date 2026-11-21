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

## Steps to run the containers locally
```Shell
# Run SGLang container on GPU 0
docker run --gpus all --rm -p 30000:30000 \
  --shm-size=16g \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  <YOUR_REGISTRY>/radix-aml-sglang:v1

# Or run vLLM container on GPU 0 (or simultaneously on GPU 1 via --gpus '"device=1"')
docker run --gpus all --rm -p 8000:8000 \
  --shm-size=16g \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  <YOUR_REGISTRY>/radix-aml-vllm:v1
```

