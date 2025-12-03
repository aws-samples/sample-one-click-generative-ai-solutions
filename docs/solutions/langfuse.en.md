# Langfuse

[Langfuse](https://langfuse.com/) is an open-source LLMOps platform that provides deep observability and analysis for generative AI applications, making evaluation, improvement, and debugging easier.

## Key Features

- **Tracing**: Complete tracking of LLM application/agent responses and tool invocations
- **Metrics Monitoring**: Monitor performance and cost-related metrics like token counts
- **Prompt Management**: Version control and deployment of prompts for LLM applications/agents
- **Playground**: Ad-hoc behavior verification with different prompts and parameters
- **Evaluation**: Create datasets from traces and execute online/offline evaluations
- **Annotation**: Provide feedback (Positive/Negative) on accumulated responses
- **Public API**: Programmatic access to Langfuse functionality

## Architecture

Deployment uses AWS Managed Services. For details, see [Hosting Langfuse V3 on Amazon ECS with Fargate using CDK Python](https://github.com/aws-samples/deploy-langfuse-on-ecs-with-fargate/tree/main/langfuse-v3). Deployment is performed using the CDK from the referenced GitHub repository.

## Deploy to AWS

Deploy using the button below. Click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">Tokyo</option>
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=LangfuseDeploymentStack&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/LangfuseDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=LangfuseDeletionStack&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/LangfuseDeploymentStack.yaml&amp;param_ExecuteDelete=true" class="deployment-button md-button md-button--danger" target="_blank">
      <i class="fa-solid fa-trash"></i>　Delete
    </a>
  </div>
  <div class="deployment-help">
    <strong>Initial Deployment:</strong> Use the Deploy button.<br>
    <strong>Complete Deletion:</strong> The Delete button removes all existing Langfuse stacks (no redeployment occurs).
  </div>
</div>

### Parameter Configuration

Configure the following parameters during deployment:

#### Notification Settings

- **NotificationEmailAddress** (required): Email address for deployment start and completion notifications

#### Deployment Options

- **ExecuteDelete** (default: false): Delete deployed Langfuse stack (warning: all data will be deleted)

#### Langfuse Configuration

- **LangfuseWorkerDesiredCount** (default: 1): Number of worker tasks for background processing
- **DatabaseInstanceType** (default: db.t4g.medium): Aurora PostgreSQL instance type
    - Options: db.t4g.medium, db.t4g.large, db.r6g.large, db.r6g.xlarge
- **CacheNodeType** (default: cache.t4g.micro): ElastiCache Redis node type
    - Options: cache.t4g.micro, cache.t4g.small, cache.t4g.medium, cache.r6g.large
- **TelemetryEnabled** (default: true): Enable Langfuse telemetry
- **ExperimentalFeaturesEnabled** (default: true): Enable experimental features

#### Initial Setup

- **OrganizationId** (default: my-org): Organization identifier
- **OrganizationName** (default: My Org): Organization display name
- **ProjectId** (default: my-project): Project identifier
- **ProjectName** (default: My Project): Project display name

### Deployment Time

- Initial deployment: 25-35 minutes
- Stack deletion: 15-20 minutes

## Usage

After deployment completes, the Langfuse URL and login credentials will be sent via email.

### 1. Login

1. Open the Langfuse URL from the email in your browser
2. Login with the email address and password provided in the email
3. **Important**: Change your password immediately after first login

### 2. Application Integration

Langfuse integrates with various agent development frameworks:

* [Amazon Bedrock AgentCore](https://langfuse.com/integrations/frameworks/amazon-agentcore)
* [Strands Agents](https://langfuse.com/integrations/frameworks/strands-agents)
* [LangChain & LangGraph Integration](https://langfuse.com/integrations/frameworks/langchain)

## Security Considerations

### Current Configuration

- Application Load Balancer is publicly accessible (0.0.0.0/0)
- Authentication handled by Langfuse application
- Secrets auto-generated and stored in AWS Secrets Manager
- All data encrypted at rest (RDS, S3, EFS)

### Production Recommendations

1. **Network Security**: Consider deploying to private subnets with VPN/Direct Connect access
2. **IP Restrictions**: Modify CDK code to add security group rules for IP allowlisting
3. **HTTPS**: Configure custom domain with ACM certificate for ALB
4. **Monitoring**: Set up CloudWatch alarms for resource utilization
5. **Backup**: Enable Aurora automated backups and regular snapshots

## Cost Optimization

### Default Configuration Cost (Estimate)

- Aurora PostgreSQL (db.t4g.medium): ~$59/month
- ElastiCache Redis (cache.t4g.micro): ~$12/month
- ECS Fargate (3 services): ~$72/month
- Application Load Balancer: ~$16/month
- Data transfer and storage: Variable

**Total: ~$160-180/month** (+ S3, EFS, data transfer)

### Optimization Tips

1. Use smaller instance types for dev/test environments
2. Enable Aurora auto-pause for non-production environments
3. Adjust worker count based on actual workload
4. Monitor and optimize S3 storage lifecycle policies

## Troubleshooting

### Deployment Issues

Check CodeBuild logs:
```bash
aws logs tail /aws/codebuild/CodeBuild-for-LangfuseDeploymentStack --follow
```

### Application Issues

Check ECS task logs in CloudWatch Logs:
- `/ecs/langfuse-web`
- `/ecs/langfuse-worker`
- `/ecs/clickhouse`

### Common Problems

1. **Deployment Timeout**: CDK bootstrap or ECR image pull may take longer than expected
2. **Database Connection Errors**: Check security group rules and Aurora status
3. **Worker Not Processing**: Verify Redis connection and worker task status

## Cleanup

1. Delete the existing deployment stack (`LangfuseDeploymentStack`)
2. Click the "Delete" button (stack name is automatically set to `LangfuseDeletionStack`)
3. Review and confirm in the CloudFormation console
4. `cdk destroy --force --all` will be executed via CodeBuild

**Warning**: All data (traces, prompts, configurations) will be deleted. Export important data before deletion.

## References

- [Langfuse Official Documentation](https://langfuse.com/docs)
- [Langfuse Self-Hosting Guide](https://langfuse.com/self-hosting)
- [GitHub Repository](https://github.com/aws-samples/deploy-langfuse-on-ecs-with-fargate)
- [GenAIOps Workshop](https://catalog.workshops.aws/genaiops-langfuse)
