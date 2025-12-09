# AI Agent Development Code Server

AI Agent Development Code Server is a pre-configured development environment with all necessary software for developing AI agents using Amazon Bedrock Agent Core. It provides a browser-based VS Code experience ([Code-Server](https://github.com/coder/code-server)) running on AWS.

## Key Features

- **Browser-Based Development Environment** - VS Code-compatible development experience via code-server
- **Pre-Configured Development Tools** - AWS CLI, SAM CLI, Kiro CLI, uv, Docker, and more included by default
- **Amazon Bedrock Agent Core Ready** - Pre-configured permissions and tools for agent development
- **Secure Access via CloudFront** - Safe HTTPS connections
- **Automated Environment Setup** - Consistent environment provisioning via SSM Document

Community Articles

* [Trying out "AI Agent Development Code Server" for One-Click Kiro-CLI Environment Setup](https://dev.classmethod.jp/articles/kiro-ai-agent-development-code-server/)

## Deploy to AWS

Click the button below to deploy. Please log in to AWS first.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">Tokyo</option>
      <option value="ap-northeast-3">Osaka</option>
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=AIAgentDevDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/AIAgentDevelopmentCodeServerDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>


### Parameter Configuration

You can configure the following parameters during deployment:

- **UserEmail** (Required)
    - User's email address. Used for Git configuration and Code Server username.
    - Deployment completion notifications will be sent to this address.
- **UserFullName** (Default: AIAgent Developer)
    - Full name used for Git configuration.
- **InstanceType** (Default: t4g.medium)
    - EC2 instance type. Uses ARM64 architecture (Graviton) instances. Use the following as a guide for performance and pricing. We recommend checking the [latest pricing information](https://aws.amazon.com/ec2/pricing/on-demand/).
    - t4g.small: 2 vCPU + 2GB memory, approximately $0.48/24 hours
    - t4g.medium: 2 vCPU + 4GB memory, approximately $0.72/24 hours
    - t4g.large: 2 vCPU + 8GB memory, approximately $1.68/24 hours
    - t4g.xlarge: 4 vCPU + 16GB memory, approximately $3.12/24 hours
- **InstanceVolumeSize** (Default: 40)
    - EBS volume size in GB.
- **HomeFolder** (Default: /workshop)
    - Working directory path. This is where repositories will be cloned.
- **RepoUrl** (Default: https://github.com/aws-samples/sample-amazon-bedrock-agentcore-onboarding.git)
    - Git repository URL to automatically clone.

### Post-Deployment Setup

After clicking the deploy button, you will receive an email titled `AI Agent Dev Code Server Deployment Notifications - Subscription Confirmation`. Click the `Confirm subscription` link to receive deployment completion notifications.

Once deployment is complete, access the browser-based development environment using the URL provided in the notification email and log in with the password.

* The password can be found in the CloudFormation Outputs
* Enable Amazon Bedrock models as needed
* Kiro CLI is pre-configured. To use it, authenticate with `kiro-cli login --use-device-flow`

### Development Environment Features

The development environment comes with the following pre-installed tools:

- **AWS Tools**: AWS CLI v2, AWS SAM CLI, Kiro CLI
- **Development Tools**: Git, Docker, Python, UV, NVM (Node.js LTS, NPM)
- **Editor**: Code-Server

Environment variables are automatically configured:

- `AWS_REGION` - Deployed region
- `AWS_ACCOUNTID` - AWS account ID

### Security

- Direct access to EC2 instances is restricted; only accessible via CloudFront
- Security groups allow only CloudFront Prefix List (configured per region)
- Passwords are securely managed in AWS Secrets Manager
- EBS volumes are encrypted
- Management access via SSM Session Manager

## Cost

Main costs come from the following resources:

- **EC2 Instance** - Charged based on t4g.medium (2 vCPU, 4GB memory) runtime (approximately $0.72 for 24 hours on-demand with t4g.medium)
- **EBS Volume** - 40GB (default) gp3 storage charges
- **CloudFront** - Charged based on data transfer volume
- **Other** - Minimal costs for VPC, Secrets Manager, SNS, etc.

You can reduce costs by stopping the EC2 instance when not in use. However, CloudFront and EBS volumes continue to incur charges even when stopped.


## Resource Cleanup

To terminate usage, delete the stack from the CloudFormation console:

1. Access the [CloudFormation Console](https://console.aws.amazon.com/cloudformation/)
2. Select the deployed stack (default: `AIAgentDevDeploymentStack`)
3. Click the "Delete" button

!!! warning "Deletion Notes"
    - Deleting the stack will also delete the EC2 instance and EBS volume
    - Back up any work in progress or data beforehand
    - Secrets Manager secrets will be deleted but have a recovery period (default 30 days)

## Additional Resources

Amazon Bedrock Agent Core hands-on is configured by default. For details, see the [README.md](https://github.com/aws-samples/sample-amazon-bedrock-agentcore-onboarding).

Also useful for book hands-on exercises:

* [AI Agent Development / Operations Introduction [Generative AI Deep Dive Guide]](https://amzn.asia/d/eX6ZBSZ)
* [AWS Generative AI App Development Practical Guide](https://amzn.asia/d/cnMEqrO)
