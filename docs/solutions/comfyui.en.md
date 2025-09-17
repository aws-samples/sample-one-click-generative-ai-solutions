# ComfyUI

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) is a node-based generative AI image generation tool that combines Stable Diffusion and various models to generate high-quality images. It's ideal for visually building complex workflows and having fine-grained control over the image generation process. For AWS deployment, you can build a scalable and cost-effective environment using [cost-effective-aws-deployment-of-comfyui](https://github.com/aws-samples/cost-effective-aws-deployment-of-comfyui).

## Key Features

- **Node-based Workflow**: Visually build workflows using drag-and-drop interface
- **Model Support**: Supports diverse models including Stable Diffusion, ControlNet, LoRA, and more
- **Custom Nodes**: Extend functionality with community-developed custom nodes
- **Batch Processing**: Efficient batch functionality for processing multiple images at once
- **API Integration**: Connect with external applications through RESTful API
- **Real-time Preview**: Monitor the generation process in real-time

## Primary Use Cases

- **Artistic Image Generation**: Create art pieces with complex styles and compositions
- **Product Design**: Generate concept art and prototype images
- **Content Creation**: Create visual materials for games, movies, and advertisements
- **Research & Development**: Experiment and test new generative technologies and models

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">Tokyo</option>
      <option value="ap-northeast-3">Osaka</option>
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=ComfyUIDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/ComfyUIDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameter Settings

You can configure the following parameters during deployment:

* **Environment**: Type of deployment environment (default: dev)
* **NotificationEmailAddress**: Email address to receive deployment notifications
* **SelfSignUp**: Enable/disable self-signup functionality (default: false)
* **AllowedSignUpEmailDomains**: Email domains allowed for signup (e.g., example1.co.jp, example2.co.jp)
* **AllowedIpV4AddressRanges**: IPv4 address ranges allowed for access (e.g., 10.0.0.100/32, 192.168.0.0/24)
* **AllowedIpV6AddressRanges**: IPv6 address ranges allowed for access

!!! warning "Security Considerations"
    For production use, the following security measures are recommended:

    1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict access to specific IP addresses
    2. **Self-Signup Control**: Set `SelfSignUp` to `false` and have administrators create users, or limit email domain by `AllowedSignUpEmailDomains` to allow signups only from specific domains
    3. **Resource Monitoring**: Regularly monitor GPU usage and costs

### Post-Deployment Setup

After clicking the deployment button, you'll receive an `AWS Notification - Subscription Confirmation` email. Click the `Confirm subscription` link to start receiving deployment status notifications.

When deployment is complete, you'll receive a notification email containing:

1. **Application URL**: Login URL to access ComfyUI
2. **User Creation Instructions**: How to create users in Amazon Cognito (if self-signup is disabled)
3. **Environment Configuration**: Details about the deployed environment
4. **AWS Cognito User Management URL**: Console link for user creation and group management

### Resource Removal

To remove deployed resources, delete the following stacks from the CloudFormation console:

1. ComfyUI main stack (includes environment name)
2. `ComfyUIDeploymentStack` deployment stack

!!! warning "Warning"
    Deleting the stacks will remove all saved images and custom settings. Please backup any necessary data beforehand.

## Usage Instructions

After logging into ComfyUI, you can start generating images by following these steps:

1. **Select Workflow**: Choose a pre-defined workflow or create a new one
2. **Configure Nodes**: Set prompts, models, parameters, and other settings
3. **Execute**: Click the "Queue Prompt" button to start image generation
4. **Review Results**: Download or save the generated images

## Troubleshooting

### Common Issues

- **Cannot login**: Verify that users are correctly created in the Cognito User Pool
- **Image generation fails**: Check GPU capacity and memory usage
- **Access denied**: Verify IP restriction settings and ensure your current IP address is allowed

### Log Verification

You can check application logs in CloudWatch Logs:

- ComfyUI application logs
- CodeBuild deployment logs
