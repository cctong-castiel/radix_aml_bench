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

## Steps to build and create containers in AWS ECR

```Shell
export AWS_REGION="ap-east-1"
export ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
export ECR_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

aws ecr get-login-password --region $AWS_REGION | \
  docker login --username AWS --password-stdin $ECR_URI

aws ecr create-repository --repository-name radix-aml-sglang --region $AWS_REGION
aws ecr create-repository --repository-name radix-aml-vllm --region $AWS_REGION

docker buildx build --platform linux/amd64 -f docker/Dockerfile.sglang \
  -t ${ECR_URI}/radix-aml-sglang:v1 --push .

docker buildx build --platform linux/amd64 -f docker/Dockerfile.vllm \
  -t ${ECR_URI}/radix-aml-vllm:v1 --push .
```
