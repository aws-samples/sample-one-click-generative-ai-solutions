# Generative AI Use Cases

[Generative AI Use Cases](https://github.com/aws-samples/generative-ai-use-cases-jp) is an application with various pre-integrated generative AI use cases. It's ideal for organizations looking to establish a safe and user-friendly environment to promote the adoption of generative AI.

## Key Features

- **Diverse Use Cases**: Experience essential generative AI applications including chat, summarization, translation, and image generation
- **RAG Functionality**: Utilize RAG capabilities to search and generate content referencing various documents
- **Secure Environment**: Implemented security features like IP restrictions and authentication for safe usage within enterprises
- **Multi-model Support**: Ability to utilize various models from Amazon Bedrock
- **Customizable**: Create and share your own use cases using the use case builder

## Organizational Use Case Scenarios

- [Streamlining Owned Media Article Creation: Salsonido Case Study](https://aws.amazon.com/jp/blogs/news/genai-case-study-salsonido/)
- [Utilized for clothing design and reduced workload by over 450 hours per month. Promoting digital talent development: Takihyo](https://aws.amazon.com/jp/solutions/case-studies/takihyo/)
- [Developed newsletter creation and proofreading tools, achieving 200 hours of monthly workload reduction: Oisix ra daichi](https://aws.amazon.com/jp/solutions/case-studies/oisix/)
    - [Presentation at AWS Summit 2025](https://youtu.be/rd8PIxrOjHw?si=wBj7wUZJXTd9CEOG)
- [Rapid proof of concept for flood detection using camera-equipped lighting: Iwasaki Electric](https://aws.amazon.com/jp/blogs/news/genai-case-study-iwasaki/)

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
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&amp;param_UsePreviousDeploymentParameter=true&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-sync"></i>　Update
    </a>
  </div>
  <div class="deployment-help">
    <strong>Initial deployment:</strong> Use the Deploy button.<br>
    <strong>Updates after deployment:</strong> Use the Update button to inherit previous settings by entering only Environment and NotificationEmailAddress (leave others as default values). (<a href="generative-ai-use-cases-update/" target="_blank">Check detailed method</a>)
  </div>
</div>

### Parameter Settings

You can configure the following parameters during deployment:

* **Environment** (default: dev)
    * The type of environment to deploy. It's the environment specified in `packages/cdk/parameter.ts`. By switching the Environment value, you can deploy multiple GenU environments.
* **NotificationEmailAddress**
    * Email address for receiving notifications about deployment start and completion
* **ModelRegion**
    * The region where Amazon Bedrock provides models. If specified models are not available in the selected region, they will be automatically converted to compatible models
* **RAGEnabled** (default: None)
    * Select RAG capabilities to enable. "Knowledge-Bases" uses Amazon Bedrock Knowledge Bases, "Kendra" uses Amazon Kendra Developer Edition, and "Both" uses both. Options with "Enterprise" suffix (like "Kendra-Enterprise") use Kendra Enterprise Edition
* **AgentCoreEnabled** (default: true)
    * Enable agent functionality that works with AWS MCP on AgentCore (runs on us-east-1)
* **SelfSignUp** (default: false)
    * Toggles self-signup functionality on/off
* **AllowedSignUpEmailDomains**
    * Sets permitted email domains separated by commas
* **AllowedIpV4AddressRanges**
    * Specifies accessible IP addresses (IPv4)
* **AllowedIpV6AddressRanges**
    * Specifies accessible IP addresses (IPv6)

!!! warning "Security Considerations"
    
    For production use, the following security measures are recommended:
    
    1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict access to specific IP addresses
    2. **Disable Self-Signup**: Set `SelfSignUp` to `false` and have administrators create users
    3. **Email Domain Restrictions**: Use `AllowedSignUpEmailDomains` to allow signups only from specific domains
    
    If IP restrictions are not set, the deployment will be publicly accessible, but since SelfSignUp is set to false by default, login requires user creation in the AWS account (via Amazon Cognito).

### Post-Deployment Setup

After clicking the deployment button, you will receive an email titled `AWS Notification - Subscription Confirmation`. Click the `Confirm subscription` link to receive deployment start and completion notifications.

When deployment is complete, you'll receive a notification email containing:

1. Application URL
2. Instructions for creating administrator accounts
3. Steps for setting up Amazon Bedrock model access

### Resource Removal

To remove deployed resources, delete both the `GenerativeAiUseCasesStack` and `GenUDeploymentStack` stacks from the CloudFormation console.

## Post-Deployment Usage

To learn how to use Generative AI Use Cases, refer to the following workshop:

* [Generative AI Experience Workshop](https://catalog.workshops.aws/generative-ai-use-cases-jp)

## Related Documentation

- [Update Guide](generative-ai-use-cases-update.en.md) - How to update existing environments
