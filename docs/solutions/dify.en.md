# Dify

[Dify](https://dify.ai) is an open-source platform for LLM application development. Through its intuitive GUI, users can easily create chatbots, agents, and complex workflows powered by generative AI. It integrates with various LLMs including Amazon Bedrock, enabling companies and developers to rapidly build and deploy their own AI applications.

## Key Features

- **Intuitive GUI Interface**: Build AI applications without coding
- **Multiple LLM Support**: Integration with various LLMs including Amazon Bedrock
- **RAG (Retrieval Augmented Generation)**: Generate accurate responses using knowledge bases
- **APIs and Plugins**: Easy integration with existing systems and feature extensions
- **Multi-step Workflows**: Visual construction of complex AI workflows
- **Self-hosting**: Secure environment built using AWS managed services

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">Virginia</option>
      <option value="ap-northeast-1">Tokyo</option>
      <option value="ap-northeast-3">Osaka</option>
      <option value="us-west-2">Oregon</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=DifyDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/DifyDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameter Settings

* **NotificationEmailAddress**
    * Email address for receiving notifications about deployment start and completion.
* **Region**
    * The AWS region where the deployment will occur.
* **AutoPause**
    * Toggles automatic database pausing ON/OFF. Recovery after automatic pause takes approximately 10 seconds.
* **AllowedIpV4Ciders**
    * Allowed IPv4 CIDR ranges for connections (e.g., 0.0.0.0/1).
* **AllowedIpV6Ciders**
    * Allowed IPv6 CIDR ranges for connections (e.g., ::/1).