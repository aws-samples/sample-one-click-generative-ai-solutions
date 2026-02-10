# GenAI Design Studio

[GenAI Design Studio](https://github.com/aws-samples/sample-genai-design-studio) is a virtual try-on solution powered by Amazon Nova Canvas. It aims to streamline various processes in the apparel industry and e-commerce services, from fashion design to actual model photography.

## Key Features

- **Model Generation**: Generate virtual model images using text prompts
- **Virtual Try-On**: High-quality clothing try-on functionality using Amazon Nova Canvas
- **Background Replacement**: Natural background replacement through text descriptions
- **Intuitive UI**: User-friendly interface for achieving professional results with simple operations
- **High-Quality Image Generation**: High-resolution image generation using Amazon Nova Canvas's latest technology

## Target Users

- **Apparel Industry**: Fashion design visualization, reducing product photography costs
- **E-commerce Services**: Enhancing customer experience through virtual try-on
- **Marketing**: Product promotion with diverse models
- **Designers**: Rapid prototyping of ideas

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">Tokyo</option>
      <option value="us-east-1">Virginia</option>
      <option value="eu-west-1">Ireland</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenStudioDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenStudioDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameter Configuration

You can configure the following parameters during deployment:

* **NotificationEmailAddress**: Email address to receive deployment start/completion notifications
* **SelfSignUp** (default: true): Enable/disable self-signup functionality
* **AllowedSignUpEmailDomains**: Allowed email domains for signup without the "@" symbol (comma-separated, e.g., example.co.jp)
* **AllowedIpV4AddressRanges** (default: 0.0.0.0/1,128.0.0.0/1): Allowed IPv4 address ranges for access
* **AllowedIpV6AddressRanges** (default: 0000:0000:0000:0000:0000:0000:0000:0000/1,8000:0000:0000:0000:0000:0000:0000:0000/1): Allowed IPv6 address ranges for access

!!! warning "Security Considerations"
    For production use, we recommend the following security measures:

    1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict accessible IP addresses
    2. **Email Domain Restrictions**: Use `AllowedSignUpEmailDomains` to allow signup only from specific domains
    3. **Self-Signup Management**: Set `SelfSignUp` to `false` if needed and have administrators create users

    If IP restrictions are not configured, the application will be deployed with public access. When `SelfSignUp` is set to false, user creation through AWS account (Amazon Cognito) is required.

### Post-Deployment Setup

After clicking the deploy button, you will receive an `AWS Notification - Subscription Confirmation` email after a short while. Click the `Confirm subscription` link to receive deployment start and completion notifications.

Once deployment is complete, you will receive a notification email containing:

1. Application URL
2. Amazon Bedrock model access setup instructions

### Resource Cleanup

To delete deployed resources, remove the following stacks from the CloudFormation console **in this order**:

1. `VtoAppStack` stack (main application) - **deployment region**
2. `VtoAppFrontendWafStack` stack (WAF for CloudFront) - **us-east-1 (N. Virginia)**
3. `GenStudioDeploymentStack` stack (deployment stack) - **deployment region**

!!! warning "Important Notes on Deletion"
    - `VtoAppFrontendWafStack` is the WAF stack for CloudFront and is **always created in us-east-1** regardless of the deployment region. When deleting, switch the CloudFormation console region to **us-east-1 (N. Virginia)**.
    - `VtoAppStack` references an exported value (WebAcl ARN) from `VtoAppFrontendWafStack`, so **`VtoAppStack` must be deleted first**.
    - If stacks are not fully deleted before redeployment, the deployment will fail due to cross-region export conflicts.
