# Bedrock Chat

[Bedrock Chat](https://github.com/aws-samples/bedrock-chat) is a multilingual generative AI platform powered by Amazon Bedrock. It supports not only simple chat functionality but also custom bot creation with knowledge bases (RAG), bot sharing through a bot store, and task automation using agents. It's ideal for those who want to understand and practically utilize the characteristics of generative AI.

## Key Features

- **Chat Functionality**: Simple chat interface powered by Amazon Bedrock foundation models
- **Custom Bot Creation**: Create bots with custom instructions and knowledge using knowledge bases (RAG)
- **Bot Store**: Share created bots among application users
- **Agent Functionality**: Automatically handle complex tasks using agent capabilities
- **API Publishing**: Publish customized bots as standalone APIs
- **Administrative Features**: API management, bot analytics, essential bot settings, and more

### Parameter Settings

You can configure the following parameters during deployment:

* **NotificationEmailAddress**: Email address to receive deployment notifications
* **BedrockRegion**: AWS region for Bedrock models (us-east-1, us-west-2, ap-northeast-1)
* **SelfSignUp**: Enable/disable self-signup functionality (default: false)
* **AllowedSignUpEmailDomains**: Email domains allowed for signup (comma separated)
* **AllowedIpV4AddressRanges**: IPv4 address ranges allowed for access (comma separated)
* **AllowedIpV6AddressRanges**: IPv6 address ranges allowed for access (comma separated)
* **EnableRagReplicas**: Enable replicas for RAG database (improves availability but increases cost)
* **Version**: Version of Bedrock Chat to deploy (default: v3)

## Security Considerations

For production use, the following security measures are recommended:

1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict access to specific IP addresses
2. **Disable Self-Signup**: Set `SelfSignUp` to `false` and have administrators create users
3. **Email Domain Restrictions**: Use `AllowedSignUpEmailDomains` to allow signups only from specific domains

## Post-Deployment Setup

When deployment is complete, you'll receive a notification email containing:

1. Frontend URL
2. Instructions for setting up Amazon Bedrock model access
3. User creation instructions (if self-signup is disabled)
4. How to add users to special groups:
    - `CreatingBotAllowed`: Permission to create custom bots
    - `Admin`: Administrator permissions
    - `PublishAllowed`: Permission to publish APIs

## Resource Removal

To remove deployed resources, delete the `BrChatDeploymentStack` stack from the CloudFormation console.
