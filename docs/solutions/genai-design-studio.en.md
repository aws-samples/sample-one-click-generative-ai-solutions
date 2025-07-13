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

### Parameter Configuration

You can configure the following parameters during deployment:

* **NotificationEmailAddress**: Email address to receive deployment start/completion notifications
* **SelfSignUp** (default: true): Enable/disable self-signup functionality
* **AllowedSignUpEmailDomains**: Allowed email domains for signup (comma-separated, e.g., example.co.jp)
* **AllowedIpV4AddressRanges** (default: 0.0.0.0/1,128.0.0.0/1): Allowed IPv4 address ranges for access
* **AllowedIpV6AddressRanges** (default: 0000:0000:0000:0000:0000:0000:0000:0000/1,8000:0000:0000:0000:0000:0000:0000:0000/1): Allowed IPv6 address ranges for access

## Security Considerations

For production use, we recommend the following security measures:

1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict accessible IP addresses
2. **Email Domain Restrictions**: Use `AllowedSignUpEmailDomains` to allow signup only from specific domains
3. **Self-Signup Management**: Set `SelfSignUp` to `false` if needed and have administrators create users

If IP restrictions are not configured, the application will be deployed with public access. When `SelfSignUp` is set to false, user creation through AWS account (Amazon Cognito) is required.

## Post-Deployment Setup

After clicking the deploy button, you will receive an `AWS Notification - Subscription Confirmation` email after a short while. Click the `Confirm subscription` link to receive deployment start and completion notifications.

Once deployment is complete, you will receive a notification email containing:

1. Application URL
2. Amazon Bedrock model access setup instructions

### Amazon Bedrock Model Access Setup

To use GenAI Design Studio, you need to enable access to Nova Canvas models in Amazon Bedrock:

1. Access the [Amazon Bedrock Console](https://console.aws.amazon.com/bedrock/)
2. Select "Model access" from the left menu
3. Enable access to the "Amazon Nova Canvas" model
4. Agree to terms of service if required

## Resource Cleanup

To delete deployed resources, remove the following stacks from the CloudFormation console:

1. `VtoAppStack` stack (main application)
2. `GenStudioDeploymentStack` stack (deployment stack)
