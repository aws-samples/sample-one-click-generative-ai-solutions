# Kiro IDE Deployment Templates

This directory contains CloudFormation templates for deploying Kiro IDE Remote on AWS with two OS options.

## Available Templates

### 1. Amazon Linux 2023 Edition (`KiroIDEDeploymentStack.yaml`)

**Best for:**
- AWS-optimized deployments
- RPM-based distribution preference
- Tighter AWS service integration

**Key Features:**
- Base OS: Amazon Linux 2023 x86_64
- Desktop: GNOME installed via dnf
- Package Manager: DNF (YUM)
- Japanese Input: ibus-anthy

### 2. Ubuntu 24.04 LTS Edition (`KiroIDEUbuntuDeploymentStack.yaml`)

**Best for:**
- Debian/Ubuntu ecosystem familiarity
- Better out-of-box GUI support
- Longer LTS support (5 years)

**Key Features:**
- Base OS: Ubuntu 24.04 LTS
- Desktop: Pre-configured GNOME (ubuntu-desktop-minimal)
- Package Manager: APT
- Japanese Input: ibus-mozc
- Streamlined setup process

## Deployment Comparison

| Feature | Amazon Linux 2023 | Ubuntu 24.04 LTS |
|---------|-------------------|------------------|
| **GUI Setup** | Manual installation | Pre-configured |
| **Package Manager** | DNF | APT |
| **LTS Duration** | ~2 years | 5 years |
| **Community** | AWS-focused | Large Ubuntu community |
| **Setup Time** | 15-20 min | 15-20 min |
| **Cost** | ~$50-60/month | ~$50-60/month |

## Quick Start

### Deploy Amazon Linux Version

```bash
aws cloudformation create-stack \
  --stack-name KiroIDE-AL2023 \
  --template-body file://KiroIDEDeploymentStack.yaml \
  --capabilities CAPABILITY_IAM \
  --parameters '[
    {"ParameterKey": "UserEmail", "ParameterValue": "your-email@example.com"},
    {"ParameterKey": "InstanceType", "ParameterValue": "t3.medium"},
    {"ParameterKey": "Language", "ParameterValue": "EN"}
  ]'
```

### Deploy Ubuntu Version

```bash
aws cloudformation create-stack \
  --stack-name KiroIDE-Ubuntu \
  --template-body file://KiroIDEUbuntuDeploymentStack.yaml \
  --capabilities CAPABILITY_IAM \
  --parameters '[
    {"ParameterKey": "UserEmail", "ParameterValue": "your-email@example.com"},
    {"ParameterKey": "InstanceType", "ParameterValue": "t3.medium"},
    {"ParameterKey": "Language", "ParameterValue": "EN"}
  ]'
```

## Parameters

Both templates share the same parameters:

| Parameter | Description | Default | Required |
|-----------|-------------|---------|----------|
| `UserEmail` | Email for notifications | - | Yes |
| `UserFullName` | Full name for Git config | Kiro IDE Developer | No |
| `InstanceType` | EC2 instance type | t3.medium | No |
| `InstanceVolumeSize` | EBS volume size (GB) | 40 | No |
| `RepoUrl` | Git repository to clone | (empty) | No |
| `Language` | OS language (EN/JP) | EN | No |

## Architecture

Both deployments create identical infrastructure:

```
Internet
    ↓
CloudFront (HTTPS)
    ↓
Application Load Balancer (HTTP)
    ↓
EC2 Instance (NICE DCV Server)
    ↓
GNOME Desktop + Kiro IDE
```

**Security:**
- CloudFront → ALB: CloudFront prefix list only
- ALB → EC2: Security group restricted
- No direct internet access to EC2

## Pre-installed Tools

Both editions include:
- **Kiro IDE**: Latest stable version
- **Kiro CLI**: Official Kiro command-line tool
- **AWS CLI v2**: Latest AWS command-line interface
- **AWS SAM CLI**: Serverless Application Model CLI
- **NVM**: Node Version Manager with LTS Node.js
- **uv**: Fast Python package installer
- **Git**: Version control system
- **Build Tools**: gcc, g++, make, etc.

## Post-Deployment

After successful deployment (15-20 minutes), you'll receive:

1. **Email notification** with access credentials
2. **CloudFormation Outputs**:
   - `KiroIDEURL`: CloudFront URL for accessing DCV
   - `Username`: Generated from your email
   - `Password`: Auto-generated secure password
   - `InstanceId`: EC2 instance identifier

## Access Instructions

1. Open the `KiroIDEURL` in your browser
2. Accept the self-signed certificate warning (first login)
3. Enter credentials when prompted:
   - **First prompt**: DCV authentication
   - **Second prompt**: OS login
   - Use the same username/password for both

## Cost Optimization

### Development Hours Only
Stop the EC2 instance when not in use:
```bash
aws ec2 stop-instances --instance-ids <InstanceId>
aws ec2 start-instances --instance-ids <InstanceId>
```

### Spot Instances
For non-production use, consider modifying the template to use Spot instances (up to 90% savings).

### Right-sizing
Monitor CPU/memory usage and adjust instance type:
- Light work: `t3.small` ($15/month)
- Standard: `t3.medium` ($30/month)
- Heavy: `t3.large` ($60/month)

## Troubleshooting

### Deployment Fails
```bash
# Check stack events
aws cloudformation describe-stack-events --stack-name <StackName>

# Check SSM command execution
aws ssm list-commands --filters "Key=ExecutionStage,Values=Failed"
```

### Cannot Access DCV
```bash
# Check instance status
aws ec2 describe-instance-status --instance-ids <InstanceId>

# Check target health
aws elbv2 describe-target-health --target-group-arn <TargetGroupArn>

# Connect via Session Manager to debug
aws ssm start-session --target <InstanceId>
```

### Password Reset
```bash
# Generate new password
NEW_PASSWORD=$(openssl rand -base64 16)

# Update secret
aws secretsmanager update-secret \
  --secret-id KiroIDE-<StackName> \
  --secret-string "$NEW_PASSWORD"

# Connect to instance and update
aws ssm start-session --target <InstanceId>
# Then run: sudo passwd <username>
```

## Validation

Both templates can be validated before deployment:

```bash
# Validate Amazon Linux template
aws cloudformation validate-template \
  --template-body file://KiroIDEDeploymentStack.yaml

# Validate Ubuntu template
aws cloudformation validate-template \
  --template-body file://KiroIDEUbuntuDeploymentStack.yaml
```

## Monitoring

### CloudWatch Logs
- DCV Server: `/aws/ssm/<InstanceId>/dcvserver`
- SSM Commands: `/aws/ssm/commands/<CommandId>`

### Metrics
```bash
# CPU utilization
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=<InstanceId> \
  --start-time 2025-01-01T00:00:00Z \
  --end-time 2025-01-02T00:00:00Z \
  --period 3600 \
  --statistics Average
```

## Cleanup

To completely remove the deployment:

```bash
aws cloudformation delete-stack --stack-name <StackName>
```

This will delete all resources except:
- CloudWatch Logs (retained for 7 days by default)
- Secrets Manager secret (can be recovered for 30 days)

## Contributing

When modifying these templates:
1. Test both AL2023 and Ubuntu variants
2. Validate templates before committing
3. Update documentation for any parameter changes
4. Maintain feature parity between editions

## References

- [Kiro Official Documentation](https://kiro.dev/docs)
- [NICE DCV User Guide](https://docs.aws.amazon.com/dcv/latest/userguide/)
- [Amazon Linux 2023 User Guide](https://docs.aws.amazon.com/linux/al2023/)
- [Ubuntu 24.04 LTS Release Notes](https://releases.ubuntu.com/24.04/)
