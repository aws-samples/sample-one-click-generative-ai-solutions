# AI Persona System

[AI Persona System](https://github.com/aws-samples/sample-ai-persona) is a sample implementation powered by Amazon Bedrock that builds AI personas and generates insights for product planning and marketing strategy through discussions, interviews, and surveys among those personas.

## Key Features

### 🎙️ Interview

Discover insights through discussions and conversations with AI personas.

- **Persona Generation**: Automatically generate AI personas from diverse data (interviews, reports, reviews, purchase data) plus natural language instructions
- **Persona Management**: Edit/delete personas, long-term memory (AgentCore Memory), knowledge and external data management
- **Discussion Modes**: Quick discussion (3-5 min), deep discussion (5-15 min), and real-time interview
- **Discussion Results**: Insight review with confidence scores, custom categories, past discussion search

### 📊 Survey

Conduct large-scale surveys with hundreds to thousands of AI personas.

- **Persona Data Setup**: Upload open datasets or proprietary customer data (CSV)
- **Template Management**: Create multiple-choice, free-text, and scale-rating questions with image attachments
- **Results**: CSV download, visual analysis (bar charts), AI insight reports

## Target Use Cases

- **Product Planning**: Validate new product ideas through discussions with AI personas
- **Marketing Strategy**: Simulate target customer reactions
- **Customer Research**: Streamline market research through large-scale surveys

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">Virginia</option>
      <option value="us-west-2">Oregon</option>
      <option value="ap-northeast-1">Tokyo</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=AIPersonaDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/AIPersonaDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameters

The following parameters can be configured during deployment.

* **NotificationEmailAddress**
    * Email address to receive deployment start/completion notifications
* **Region** (default: us-east-1)
    * Deployment region (us-east-1, us-west-2, ap-northeast-1)
* **EnableLongTermMemory** (default: true)
    * Enable/disable AgentCore Memory for long-term memory feature
* **EnableWaf** (default: false)
    * Enable AWS WAF on CloudFront for additional security (rate limiting and managed rules)
* **SelfSignUp** (default: false)
    * Enable/disable Cognito self-signup
* **AllowedIpAddresses**
    * Allowed IPv4 CIDR ranges for access restriction (comma separated, e.g. 203.0.113.0/24,198.51.100.1/32). WAF is automatically enabled when specified.

!!! warning "Security Note"
    
    For production use, the following security measures are recommended:
    
    1. **IP Restriction**: Use `AllowedIpAddresses` to restrict accessible IP addresses
    2. **Disable Self-Signup**: Set `SelfSignUp` to `false` and have administrators create users
    
    Without IP restriction, the application is deployed with public access, but since SelfSignUp defaults to false, user creation via AWS account (Amazon Cognito) is required to log in.

## Post-Deployment Setup

### User Management

1. Access the user management console URL provided in the deployment completion notification email
2. Create users in the Amazon Cognito User Pool (users can self-register if self-signup is enabled)
3. Log in from the application URL

### Accessing the Application

After deployment is complete, access the application via the CloudFront domain URL provided in the notification email.

## More Information

For detailed technical information and development guides, please refer to the [GitHub repository](https://github.com/aws-samples/sample-ai-persona).
