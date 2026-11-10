# AWS Container Demo - Frontend + Backend - ECR + EKS + Helm + Istio
NOT ECS. Registry is ECR (Elastic Container Registry). Only deploy target is EKS.

Flow: GitHub push -> CodePipeline -> CodeBuild (build 2 Docker images, push to ECR) -> Helm upgrade to EKS -> Istio Gateway/VirtualService/DestinationRule (80/20 canary)

Frontend (Flask, :8080) calls Backend (Flask API, :8080 /api/data, /health). APP_ENV + APP_VERSION shown on page for proof.
Images: <account>.dkr.ecr.ap-south-1.amazonaws.com/demo-frontend:<tag> and demo-backend:<tag>
Local test: docker compose up --build -> http://localhost:8080
