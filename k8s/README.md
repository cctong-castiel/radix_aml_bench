# Create EKS cluster

## Steps to create EKS cluster

```Shell
eksctl create cluster -f k8s/cluster.yaml
aws eks update-kubeconfig --name radix-aml-eks --region ap-east-1
```
