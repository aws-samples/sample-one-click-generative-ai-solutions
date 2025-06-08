# Generative AI Use Cases

[Generative AI Use Cases](https://github.com/aws-samples/generative-ai-use-cases-jp) is an application with various pre-integrated generative AI use cases. It's ideal for organizations looking to establish a safe and user-friendly environment to promote the adoption of generative AI.

## Key Features

- **Diverse Use Cases**: Experience essential generative AI applications including chat, summarization, translation, and image generation
- **RAG Functionality**: Utilize RAG capabilities to search and generate content referencing various documents
- **Secure Environment**: Implemented security features like IP restrictions and authentication for safe usage within enterprises
- **Multi-model Support**: Ability to utilize various models from Amazon Bedrock
- **Customizable**: Create and share your own use cases using the use case builder

### Parameter Settings

You can configure the following parameters during deployment:

* **Environment** (default: dev)
   * The type of environment to deploy. It's the environment specified in `packages/cdk/parameter.ts`. By switching the Environment value, you can deploy multiple GenU environments.
* **NotificationEmailAddress**
   * Email address for receiving notifications about deployment start and completion
* **ModelRegion**
   * The region where Amazon Bedrock models will be used
* **RAGEnabled** (default: false)
   * Enables RAG (Retrieval-Augmented Generation) for Knowledge Base
* **SelfSignUp** (default: false)
   * Toggles self-signup functionality on/off
* **AllowedSignUpEmailDomains**
   * Sets permitted email domains separated by commas
* **AllowedIpV4AddressRanges**
   * Specifies accessible IP addresses (IPv4)
* **AllowedIpV6AddressRanges**
   * Specifies accessible IP addresses (IPv6)

## Security Considerations

For production use, the following security measures are recommended:

1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict access to specific IP addresses
2. **Disable Self-Signup**: Set `SelfSignUp` to `false` and have administrators create users
3. **Email Domain Restrictions**: Use `AllowedSignUpEmailDomains` to allow signups only from specific domains

If IP restrictions are not set, the deployment will be publicly accessible, but since SelfSignUp is set to false by default, login requires user creation in the AWS account (via Amazon Cognito).

## Post-Deployment Setup

After clicking the deployment button, you will receive an email titled `AWS Notification - Subscription Confirmation`. Click the `Confirm subscription` link to receive deployment start and completion notifications.

When deployment is complete, you'll receive a notification email containing:

1. Application URL
2. Instructions for creating administrator accounts
3. Steps for setting up Amazon Bedrock model access

## Learning Resources

To learn how to use Generative AI Use Cases, refer to the following workshop:

* [Exploring Generative AI Use Cases with GenU](https://catalog.us-east-1.prod.workshops.aws/workshops/58088ef5-d47c-441d-ae65-e44ff1d6a92b/en-US)

## Related Documentation

- [Update Guide](generative-ai-use-cases-update.en.md) - How to update existing environments

## Resource Removal

To remove deployed resources, delete both the `GenerativeAiUseCasesStack` and `GenUDeploymentStack` stacks from the CloudFormation console.
