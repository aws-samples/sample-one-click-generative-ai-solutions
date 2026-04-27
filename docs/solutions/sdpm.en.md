# Spec-Driven Presentation Maker (SDPM)

[Spec-Driven Presentation Maker](https://github.com/aws-samples/sample-spec-driven-presentation-maker) is an open-source toolkit for creating presentations using a spec-driven development approach. Design 'what to convey' first, and let AI build 'how to present it'.

## Key Features

- **Spec-Driven Design**: Define logical structure as a specification from source materials
- **AI Auto-Build**: AI automatically builds slides following templates
- **4-Layer Architecture**: From Kiro CLI skill to full-stack web app
- **MCP Support**: Available with Claude Desktop, VS Code, Kiro and other MCP clients

![SDPM Workflow](../assets/images/solutions/sdpm/workflow-en.png)

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
      <option value="ap-northeast-1">Tokyo</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=SdpmDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/SdpmDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameter Settings

You can configure the following parameters during deployment:

* **NotificationEmailAddress**: Email address to receive deployment notifications
* **DeploymentLayer**: Deployment layer (default: layer4)
    - `layer3`: MCP Server only
    - `layer4`: Full stack with Agent + Web UI
* **SearchSlides**: Enable semantic slide search (default: false). Uses Bedrock Knowledge Base
* **Observability**: Enable Bedrock Model Invocation Logging (default: false)

!!! warning "Security Considerations"
    For production use, the following security measures are recommended:

    1. **IP Restrictions**: Restrict access to specific IP addresses
    2. **Disable Self-Signup**: Have administrators create users
    3. **Email Domain Restrictions**: Allow signups only from specific domains

### Post-Deployment Setup

After clicking the deployment button, you will receive an email titled `AWS Notification - Subscription Confirmation` after a short while. Click the `Confirm subscription` link to start receiving deployment start and completion notifications.

When deployment is complete, you'll receive a notification email containing:

1. CloudFront URL
2. Instructions for creating users in Cognito

**For Layer 4 (Full Stack):**

1. Create a user in Amazon Cognito
2. Access the web app via the CloudFront URL

**For Layer 3 (MCP Server Only):**

1. Connect to the deployed MCP server endpoint using an MCP client (Claude Desktop, VS Code, Kiro, etc.)

### Resource Removal

To remove deployed resources, delete the following stacks from the CloudFormation console in reverse dependency order:

1. `SdpmWebUi`
2. `SdpmAgent`
3. `SdpmRuntime`
4. `SdpmData`
5. `SdpmAuth`
6. `SdpmDeploymentStack`
