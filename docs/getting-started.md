# Getting Started

This guide will help you prepare your AWS account and deploy your first generative AI solution with just a few clicks.

## Step 1: Prepare Your AWS Account

Before deploying any solutions, ensure your AWS account meets the following requirements:

### Required Permissions

You'll need an IAM user or role with permissions to create the following resources:
- CloudFormation stacks
- Lambda functions
- IAM roles and policies
- S3 buckets
- API Gateway endpoints
- Amazon Bedrock model access

If you're not an administrator, ask your AWS administrator to grant you the necessary permissions or to deploy the solution for you.

### Quick Setup for Administrators

If you have administrator access, you can use the following quick setup option:

<a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=generative-ai-prerequisites" class="quick-launch-btn">
  <i class="fa-solid fa-shield btn-icon"></i>Deploy Prerequisites Stack
</a>

This stack creates all necessary permissions and enables required services.

### AWS Regions

Most solutions in this catalog are available in the following AWS regions:
- US East (N. Virginia)
- US West (Oregon)
- Europe (Ireland)
- Asia Pacific (Tokyo)

Make sure to select a supported region before deployment.

## Step 2: Model Access

Many solutions use foundation models from Amazon Bedrock. You need to request access to these models before deployment:

1. Go to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock)
2. Click "Model access" in the left navigation
3. Request access to the following models:
   - Anthropic Claude 3 Sonnet
   - Amazon Titan Text
   - Stability AI Stable Diffusion XL (if you need image generation)

<div style="padding: 20px; background-color: #f8f9fa; border-radius: 8px; margin: 20px 0; border-left: 4px solid #6366f1;">
  <strong>Note:</strong> Model access requests are typically approved within minutes, but may take up to 24 hours in some cases.
</div>

## Step 3: Choose Your Solution

Browse our solutions and select the solution that best fits your needs.

We recommend starting with one of these beginner-friendly options:

<div class="solution-card">
  <div class="solution-card__content">
    <div class="solution-card__title">Generative AI Use Cases</div>
    <div class="solution-card__description">
      A collection of ready-to-use AI functions with a simple interface. Perfect for exploring what generative AI can do.
    </div>
    <div class="solution-card__actions">
      <a href="solutions/generative-ai-use-cases/" class="detail-button">
        <span class="twemoji">
          {% include ".icons/fontawesome/solid/circle-info.svg" %}
        </span>
        View Details
      </a>
    </div>
  </div>
</div>

<div class="solution-card">
  <div class="solution-card__content">
    <div class="solution-card__title">Dify</div>
    <div class="solution-card__description">
      A visual AI workflow builder that makes it easy to create custom AI applications without coding.
    </div>
    <div class="solution-card__actions">
      <a href="solutions/dify/" class="detail-button">
        <span class="twemoji">
          {% include ".icons/fontawesome/solid/circle-info.svg" %}
        </span>
        View Details
      </a>
    </div>
  </div>
</div>

## Step 4: Deploy with One Click

Each solution page has a "Quick Launch" button that will take you to the AWS CloudFormation console with the template pre-loaded.

To deploy:

1. Click the "Quick Launch" or "Deploy to AWS" button on the solution page
2. Review the stack details in the CloudFormation console
3. Check the acknowledgment at the bottom of the page
4. Click "Create stack"

<div style="padding: 20px; background-color: #f8f9fa; border-radius: 8px; margin: 20px 0; border-left: 4px solid #10b981;">
  <strong>Tip:</strong> Deployment typically takes 10-30 minutes depending on the solution. You can monitor progress in the CloudFormation console.
</div>

## Step 5: Access Your Solution

After deployment completes:

1. Go to the "Outputs" tab of your CloudFormation stack
2. Look for a URL labeled "WebInterface", "Dashboard", or similar
3. Click the URL to access your solution

Each solution includes post-deployment instructions on its detail page.

## Common Questions

<details>
  <summary><strong>How much will this cost?</strong></summary>
  <p>The cost depends on the solution and your usage. Most solutions use serverless resources that scale with usage. Each solution page includes cost estimates and pricing information.</p>
</details>

<details>
  <summary><strong>Is my data secure?</strong></summary>
  <p>Yes! All solutions deploy to YOUR AWS account, meaning you maintain complete control over your data. No data is shared with third parties unless you explicitly configure external integrations.</p>
</details>

<details>
  <summary><strong>What if I need help?</strong></summary>
  <p>Each solution includes links to documentation, support channels, and community resources. You can also contact AWS Support if you have an AWS Support plan.</p>
</details>

<details>
  <summary><strong>Can I customize these solutions?</strong></summary>
  <p>Absolutely! Each solution includes source code and documentation for customization. You can modify the solutions to fit your specific needs.</p>
</details>

## Next Steps

Ready to start your generative AI journey? Choose a solution from our catalog and deploy it with just one click!

<a href="/solutions/" class="md-button md-button--primary" style="display: inline-block; padding: 0.5rem 1rem; font-size: 0.9rem;">Browse Solutions</a>
