# Remote SWE Agents

[Remote SWE Agents](https://github.com/aws-samples/remote-swe-agents) is an example implementation of a fully autonomous software development AI agent. The agent works in its own dedicated development environment, freeing you from being tied to your laptop!

This is a self-hosted, fully open-source solution on AWS that offers a similar experience to cloud-based asynchronous coding agents, such as Devin, OpenAI Codex, or Google Jules.

## Key Features

- **Fully autonomous software development agent** - AI-powered development workflow automation
- **Web-based management interface** - Modern Next.js webapp for session management and real-time monitoring
- **Comprehensive API** - RESTful endpoints for programmatic integration and session control
- **Powered by AWS serverless services** with minimal maintenance costs
- **No upfront or fixed costs** while you don't use the system
- **Efficient token usage** with prompt cache and middle-out strategy

### Parameters

- **NotificationEmailAddress**
    - Email address to receive deployment notifications. This address will also be used as the initial webapp user.
- **GitHubAccessTokenValue**
    - GitHub Personal Access Token (PAT) used by the agent to access GitHub repositories.
- **TargetEnv** (default: Prod)
    - Environment name for deployment. If you want to deploy multiple environments, set a unique value for each environment.
- **AllowedIpV4AddressRanges**
    - Comma-separated list of IPv4 CIDR ranges that can access the webapp.
- **AllowedIpV6AddressRanges**
    - Comma-separated list of IPv6 CIDR ranges that can access the webapp.
- **WorkerAdditionalPolicies**
    - Comma-separated list of additional IAM managed policies to attach to the worker instance.

## Prerequisites

- AWS account
- GitHub account

## Post-Deployment Usage

After deployment is complete, you can access the webapp via the URL provided in the notification email. Initial user credentials will be sent to the same email address.

From the webapp, you can:

- Create and manage agent sessions
- Connect to GitHub repositories
- Monitor agent activities in real-time

### Slack Integration Setup (Optional)

To enable Slack integration for interacting with the agent:

1. **Configure Slack Bolt App**: Use the API endpoint provided in the notification email to set up your Slack Bolt App. Refer to [the solution's README.md](https://github.com/aws-samples/remote-swe-agents/blob/main/README.md) for detailed configuration instructions.

2. **Update SSM Parameters**: After creating your Slack app, update the following SSM parameters with your app credentials:
    - Navigate to [AWS Systems Manager Parameters](https://console.aws.amazon.com/systems-manager/parameters/)
    - Update `/remote-swe/slack/bot-token` with your BOT TOKEN
    - Update `/remote-swe/slack/signing-secret` with your SIGNING SECRET

3. **Redeploy Configuration**: From the [CodeBuild console](https://console.aws.amazon.com/codesuite/codebuild/projects), start a new build for the `RemoteSweDeployment` project to apply the Slack configuration.

Once deployment is complete, you can mention the Slack app to interact with the agent directly from Slack.

## Cost

Remote SWE Agents follows a pay-as-you-go model. Costs are nearly zero when not in use and are only incurred during active sessions. Resources used include EC2 instances, EBS volumes, Bedrock API calls, and more.

![architecture](https://raw.githubusercontent.com/aws-samples/remote-swe-agents/refs/heads/main/docs/imgs/architecture.png)

## Additional Resources

Please refer to [the solution's README.md](https://github.com/aws-samples/remote-swe-agents/blob/main/README.md) for more details.
