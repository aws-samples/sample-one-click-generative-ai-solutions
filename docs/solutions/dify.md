# Dify

Powerful workflow builder for enhanced generative AI with multiple connectors.

## Overview

Dify is an open-source LLMOps platform that allows you to build powerful AI workflows with a visual interface. Our one-click AWS deployment provides a fully managed Dify instance in your own AWS account, giving you complete control and ownership of your data.

<div style="display: flex; gap: 20px; margin: 30px 0; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <img src="/assets/images/dify-1.png" alt="Dify Workflow Builder" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
  <div style="flex: 1; min-width: 300px;">
    <img src="/assets/images/dify-2.png" alt="Dify Applications" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

## Key Features

- **Visual AI Workflow Builder**: Create complex AI workflows without coding
- **Multiple LLM Support**: Connect to Amazon Bedrock, SageMaker, or bring your own models
- **Data Connectors**: Integrate with your databases, S3 buckets, and APIs
- **Team Collaboration**: Built-in versioning and team management features
- **Prompt Management**: Library of reusable prompt templates
- **Web UI & API Access**: Use via browser interface or integrate with your applications
- **Logging & Analytics**: Track usage, performance, and costs

## Use Cases

- **Customer Support Automation**: Build AI agents that can handle customer inquiries
- **Content Generation**: Create marketing copy, product descriptions, and more
- **Research Assistants**: Develop AI-powered research tools to analyze documents and data
- **Internal Knowledge Bases**: Create AI interfaces for company documentation
- **Data Analysis**: Build workflows that analyze and summarize complex data

## Architecture

Our Dify deployment uses a containerized architecture running on Amazon ECS with a PostgreSQL database for storage. All components are deployed within your AWS account with appropriate security settings.

<img src="/assets/images/dify-architecture.png" alt="Dify Architecture Diagram" style="max-width: 100%; margin: 30px 0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

## Deployment Options

### Quick Launch

Deploy Dify to your AWS account with a single click:

<a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=dify" class="quick-launch-btn" style="margin-bottom: 20px;">
  <i class="fa-solid fa-rocket btn-icon"></i>Deploy to AWS (Standard Configuration)
</a>

The standard configuration includes:
- Dify application and database
- Amazon Cognito for user authentication
- Integration with Amazon Bedrock models
- Automatic scaling based on usage

### Advanced Deployment

For more customization options:

<a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=dify-custom" class="quick-launch-btn" style="margin-bottom: 20px;">
  <i class="fa-solid fa-cog btn-icon"></i>Deploy with Custom Configuration
</a>

The custom configuration allows you to:
- Select which LLM providers to enable
- Configure custom VPC settings
- Set up custom domain and SSL certificates
- Adjust compute and database resources

## Getting Started After Deployment

After deployment (approximately 20-30 minutes), you'll be able to access your Dify instance at the URL provided in the CloudFormation outputs.

Follow these steps to get started:
1. Create an admin account
2. Configure your LLM providers
3. Create your first application
4. Add data sources and connectors
5. Build and publish your first AI workflow
