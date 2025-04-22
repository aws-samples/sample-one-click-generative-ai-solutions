# Generative AI Use Cases

Ready-to-use generative AI functions with enterprise-grade security features.

## Overview

The Generative AI Use Cases solution provides a comprehensive set of AI capabilities that you can deploy to your AWS account with a single click. This solution includes several pre-built AI functions that are ready to use without requiring prompt engineering expertise.

<div style="display: flex; gap: 20px; margin: 30px 0; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <img src="/assets/images/generative-ai-use-cases-1.png" alt="Generative AI Use Cases Dashboard" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
  <div style="flex: 1; min-width: 300px;">
    <img src="/assets/images/generative-ai-use-cases-2.png" alt="Generative AI Use Cases Text Generation" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

## Key Features

- **Prompt-less Operation**: Use AI capabilities without needing to craft perfect prompts
- **Enterprise Security**: Built-in authentication, encryption, and access controls
- **Pre-built Functions**:
  - Text summarization
  - Content generation
  - Sentiment analysis
  - Document analysis
  - Code generation
  - Image generation (optional)
- **Customizable**: Extend with your own functions or modify existing ones
- **Scalable Architecture**: Built on serverless AWS services to scale with your needs
- **Usage Analytics**: Track and optimize your AI usage

## Architecture

This solution deploys a set of AWS Lambda functions, a secure API Gateway, S3 buckets for storage, and an optional SageMaker endpoint for custom models. All components are fully managed and secured.

<img src="/assets/images/generative-ai-use-cases-architecture.png" alt="Architecture Diagram" style="max-width: 100%; margin: 30px 0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Deployment Options

### Quick Launch

Deploy this solution to your AWS account with a single click:

<a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=generative-ai-use-cases" class="quick-launch-btn" style="margin-bottom: 20px;">
  <i class="fa-solid fa-rocket btn-icon"></i>Deploy to AWS (Default Configuration)
</a>

This option will deploy the solution with default settings, including:
- Text and document analysis functions
- Amazon Bedrock as the foundation model provider
- Basic authentication

### Advanced Deployment Options

For more customization options:

<a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=generative-ai-use-cases-custom" class="quick-launch-btn" style="margin-bottom: 20px;">
  <i class="fa-solid fa-cog btn-icon"></i>Deploy with Custom Configuration
</a>

The custom configuration allows you to:
- Select which functions to deploy
- Choose between different foundation models
- Configure advanced security options
- Set up integration with existing AWS services

## Getting Started After Deployment

After deployment completes (approximately 10-15 minutes), you'll receive an email with:

1. The URL to access your solution dashboard
2. Initial admin credentials
3. Documentation links

Follow the post-deployment steps to:
1. Change the default password
2. Create additional user accounts
3. Configure API access if needed
4. Explore the available AI functions

## Support and Resources

- [Detailed Documentation](https://docs.aws.amazon.com/generative-ai-use-cases)
- [GitHub Repository](https://github.com/aws-samples/generative-ai-use-cases)
- [Community Forum](https://repost.aws/tags/generative-ai)
- [AWS Support](https://aws.amazon.com/support)
