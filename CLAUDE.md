# CLAUDE.md - CloudFormation One-Click Deployment Context

This project provides CloudFormation templates for one-click deployment of generative AI solutions. When working on deployment templates, follow these key guidelines:

## Core Architecture Pattern

All one-click deployments follow this pattern:
1. User deploys CloudFormation stack
2. Stack creates SNS topic, CodeBuild project, and Lambda trigger
3. Lambda automatically triggers CodeBuild
4. CodeBuild clones repo, updates parameters, deploys application stack
5. Notifications sent via SNS at start and completion

## Key Implementation Rules

### Required Components
- **SNS Topic**: For deployment notifications (email subscription)
- **CodeBuild Project**: With IAM roles, environment variables from CF parameters
- **Lambda Custom Resource**: Auto-triggers CodeBuild on stack creation
- **IAM Roles**: For CodeBuild and Lambda with least privilege

### Parameter Guidelines
- **Required**: `NotificationEmailAddress` (with email validation pattern)
- **Optional with defaults**: Environment, regions, security settings
- **Validation**: Use AllowedPattern, AllowedValues, ConstraintDescription

### CodeBuild BuildSpec Structure
1. **Install**: Setup runtime, clone repo, install dependencies
2. **Pre-build**: Update application parameters
3. **Build**: Check/run CDK bootstrap, deploy application stack
4. **Post-build**: Send completion notification with app details

### Best Practice: Parameter Extraction
✅ **RECOMMENDED**: Use CloudFormation outputs
```bash
STACK_NAME=$(aws cloudformation describe-stacks --query "Stacks[?contains(StackName, 'AppPattern')].StackName" --output text)
APP_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?contains(OutputKey, 'FrontendUrl')].OutputValue" --output text)
```

❌ **AVOID**: Parsing temporary files like .cdk-outputs.json

### Security Best Practices
- Default to restrictive IP ranges with clear warnings for public access
- Disable self-signup by default
- Require domain restrictions when self-signup enabled
- Use least privilege IAM permissions

### Error Handling
- Custom resource must handle and report errors properly
- Include meaningful error messages in CodeBuild scripts
- Test parameter extraction queries independently before embedding

## Development Commands

### Deployment (use JSON format for complex parameters)
```bash
aws cloudformation create-stack \
  --stack-name XXXX \
  --template-body file://XXXX.yaml \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters '[
    {"ParameterKey": "NotificationEmailAddress", "ParameterValue": "email@example.com"},
    {"ParameterKey": "AllowedSignUpEmailDomains", "ParameterValue": "example.com,example.co.jp"}
  ]'
```

### Monitoring
```bash
# Stack status
aws cloudformation describe-stacks --stack-name XXXX

# CodeBuild logs
aws logs tail /aws/codebuild/<PROJECT_NAME> --follow

# Debug outputs
aws cloudformation describe-stacks --stack-name <STACK_NAME> --query "Stacks[0].Outputs"
```

### Validation & Testing
```bash
# Validate template
aws cloudformation validate-template --template-body file://XXXX.yaml

# Delete stack
aws cloudformation delete-stack --stack-name XXXX
```

## Adapting for New Applications

1. Analyze application architecture using MCP tools
2. Identify required parameters (config, security, features, integrations)
3. Copy existing template (e.g., `deployments/genu/GenUDeploymentStack.yaml`) and modify
4. Test deployment scenarios with various parameter combinations

## Project Structure
- Main deployment templates are in `deployments/` directory
- Each solution has its own subdirectory (e.g., `genu/`, `dify/`)
- Follow existing patterns for consistency