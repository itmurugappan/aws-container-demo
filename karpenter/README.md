BASIC KARPENTER - install (after cluster is up, Helm):
1. Tag subnets + SG for discovery: eksctl create cluster already tags VPC resources; add tag karpenter.sh/discovery=aws-eks-demo to cluster subnets and the cluster security group (eksctl sets this tag automatically on its VPC when --tags used; verify in console if NodeClass stays NotReady).
2. IAM: controller needs a role (IRSA) to call EC2 RunInstances; nodes need KarpenterNodeRole with AmazonEKSWorkerNodePolicy, AmazonEKS_CNI_Policy, AmazonEC2ContainerRegistryReadOnly, AmazonSSMManagedInstanceCore. eksctl utils / the Karpenter getting-started CloudFormation creates both.
3. helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter --namespace kube-system --set "settings.clusterName=aws-eks-demo" --set controller.resources.requests.cpu=1 --set controller.resources.requests.memory=1Gi
   (Karpenter controller itself runs on the managed node group - it cannot provision its own first node.)
4. kubectl apply -f karpenter/ec2nodeclass.yaml -f karpenter/nodepool.yaml
5. PROOF: kubectl apply -f karpenter/inflate.yaml; kubectl get nodes -w (new node in ~60s); kubectl delete -f karpenter/inflate.yaml; watch node disappear (consolidation).
Concepts: NodePool = WHO Karpenter may provision (instance types, capacity, limits). EC2NodeClass = HOW in AWS terms (AMI, subnets, SG, node role). No node group sizing math - it is just-in-time, pod-driven provisioning. Replaces Cluster Autoscaler + fixed ASGs for most workloads.
