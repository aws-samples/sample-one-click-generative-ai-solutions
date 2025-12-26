# Kiro IDE Remote - Ubuntu Edition

[Kiro](https://kiro.dev/) is an integrated development environment suitable for building Enterprise Ready applications that support the entire development process starting from specification definition. This Ubuntu edition provides a streamlined deployment experience using **Ubuntu 24.04 LTS** with **pre-configured GNOME desktop**, making it easier to set up GUI applications compared to Amazon Linux 2023.

![overview](../assets/images/solutions/kiro-ide/kiro-ide-remote.png)

## Key Differences from Amazon Linux Version

This Ubuntu variant offers several advantages:

- **Pre-installed GUI Support**: Ubuntu Desktop comes with GNOME pre-configured, reducing setup complexity
- **APT Package Manager**: Familiar package management for Ubuntu/Debian users
- **Better GUI Application Support**: Ubuntu Desktop is optimized for GUI applications out of the box
- **Streamlined Installation**: Fewer steps required to get a working desktop environment

## Key Features

- **Cloud-based Development Environment**: Remote desktop environment accessible from a browser
- **Ubuntu 24.04 LTS**: Long-term support with extensive community resources
- **High-speed Connection via Amazon DCV**: Provides a comfortable development experience with low latency
- **Pre-installed Development Tools**: Kiro CLI, AWS CLI, AWS SAM CLI, uv, NVM, and more are available
- **Language Support**: Pre-configured for English or Japanese
- **Secure Access**: Safe connection via CloudFront and ALB

## Deploy to AWS

You can deploy using the button below. Click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
      <option value="ap-northeast-1">Tokyo</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=KiroIDEUbuntuDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/KiroIDEUbuntuDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy Ubuntu Edition
    </a>
  </div>
</div>

### Parameter Settings

* **UserEmail**
    * User's email address. Used for notification delivery and system configuration.
* **UserFullName**
    * User's full name. Used for Git configuration and other settings (default: Kiro IDE Developer).
* **InstanceType**
    * EC2 instance type (default: t3.medium).
* **InstanceVolumeSize**
    * EBS volume size in GB (default: 40).
* **RepoUrl**
    * Git repository URL to automatically clone for development (optional).
* **Language**
    * OS language setting. Choose EN (English) or JP (Japanese) (default: EN).

When deployment starts, an email will be sent to the email address set in `UserEmail` to enable notification subscription. Please subscribe from the email to receive notifications.

## Technical Details

### Operating System
- **Base OS**: Ubuntu 24.04 LTS (Long Term Support)
- **Desktop Environment**: GNOME Shell (ubuntu-desktop-minimal)
- **Remote Access**: NICE DCV Server with web viewer

### Pre-installed Tools
- **Development IDEs**: Kiro IDE
- **Cloud Tools**: AWS CLI v2, AWS SAM CLI
- **Version Managers**: NVM (Node Version Manager), uv (Python package manager)
- **Build Tools**: Git, build-essential, gcc, g++, make
- **CLI Tools**: Kiro CLI, jq, curl, wget

### Japanese Language Support
When Language parameter is set to "JP":
- Japanese language packs and fonts (Noto CJK)
- Japanese input method (ibus-mozc)
- Timezone set to Asia/Tokyo
- Locale set to ja_JP.UTF-8

## Access After Deployment

When deployment is complete, you will receive an email with the following information. You can also check it from the Outputs tab in CloudFormation.

- **KiroIDEURL**: Access URL to Kiro IDE
- **Username**: Login username
- **Password**: Login password
- **InstanceId**: EC2 instance ID

Access the URL and log in with the displayed username and password.

### Access Notes
* You will be prompted to log in twice - once for Amazon DCV and once for the OS - but the password is the same for both.
* If the font appears stretched when opening a terminal in Kiro, open `File > Preference > Settings`, search for `terminal spacing`, and adjust the `Integrated: Letter Spacing` value to around -2 to -3.
* If authentication with Kiro CLI is slow to proceed, try `kiro-cli login --use-device-flow`.

## Architecture

The deployment creates:
1. **VPC** with 2 public subnets across 2 availability zones
2. **EC2 Instance** running Ubuntu 24.04 LTS with GNOME desktop
3. **Application Load Balancer** to distribute traffic
4. **CloudFront Distribution** for global access and HTTPS termination
5. **NICE DCV Server** for high-performance remote desktop streaming
6. **Security Groups** restricting access to CloudFront only

## Deployment Time

Expect approximately 15-20 minutes for complete deployment, including:
- Stack creation (5 minutes)
- Ubuntu Desktop installation (5-7 minutes)
- NICE DCV and Kiro IDE setup (5-8 minutes)
- System reboot and health checks (2-3 minutes)

## Cost Estimation

Typical monthly costs (us-east-1):
- **EC2 t3.medium**: ~$30/month
- **EBS gp3 40GB**: ~$3/month
- **ALB**: ~$20/month
- **CloudFront**: Minimal (depends on usage)
- **Data Transfer**: Varies by usage

**Total**: Approximately $50-60/month for the base infrastructure

## Troubleshooting

### Deployment Fails
- Check CloudFormation Events tab for specific errors
- Ensure your AWS account has necessary permissions (EC2, VPC, IAM, CloudFormation, etc.)
- Verify SSM agent connectivity in Systems Manager

### Cannot Access DCV URL
- Wait a few minutes after deployment completes for all services to start
- Check EC2 instance is running and healthy in target group
- Review CloudWatch Logs for DCV server logs

### Desktop Environment Not Loading
- Connect to instance via Systems Manager Session Manager
- Check systemd service status: `systemctl status dcvserver`
- Review DCV logs: `journalctl -u dcvserver`

## Comparison: Amazon Linux vs Ubuntu

| Feature | Amazon Linux 2023 | Ubuntu 24.04 LTS |
|---------|-------------------|------------------|
| Desktop Installation | Manual (dnf groupinstall) | Pre-configured (ubuntu-desktop) |
| Package Manager | DNF | APT |
| GUI App Support | Requires additional setup | Optimized out-of-box |
| Community Support | AWS-focused | Large Ubuntu community |
| LTS Support | ~2 years | 5 years |
| Japanese Input | ibus-anthy | fcitx5-mozc |

## When to Use Ubuntu Edition

Choose the Ubuntu edition when:
- You're more familiar with Debian/Ubuntu ecosystem
- You need better out-of-box GUI application support
- You prefer APT package manager
- You want longer LTS support (5 years)
- You're developing applications targeting Ubuntu

Choose the Amazon Linux edition when:
- You're optimizing for AWS-specific features
- You prefer RPM-based distributions
- You want tighter integration with AWS services
- Your production environment uses Amazon Linux

## Related Links

- [Kiro Official Website](https://kiro.dev/)
- [Amazon DCV](https://aws.amazon.com/hpc/dcv/)
- [Ubuntu 24.04 LTS Release Notes](https://releases.ubuntu.com/24.04/)
