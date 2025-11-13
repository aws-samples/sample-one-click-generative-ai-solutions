# Review & Assessment Powered by Intelligent Documentation (RAPID)

[RAPID](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation) is a document review solution powered by generative AI (Amazon Bedrock). It streamlines review processes involving extensive documents and complex checklists using a Human in the Loop approach. It supports the entire process from checklist structuring to AI-assisted review and final human judgment, reducing review time and improving quality.

## Key Features

- **Checklist Structuring**: Automatically structures complex checklists into AI-understandable formats
- **AI-Powered Document Review**: Leverages Amazon Bedrock to automatically analyze and evaluate document content
- **Human in the Loop**: Framework for humans to review and modify AI judgment results
- **Review Result Visualization**: Displays review results in an easy-to-understand format to support efficient verification work
- **Batch Processing Support**: Capable of processing large volumes of documents in batches
- **Customizable**: Checklists can be customized according to industry and use case requirements

## Key Use Cases

* **Product Specification Compliance Review**
   * Efficiently verify that product development specifications meet requirements and industry standards. Automate the process of comparing thousands of specifications annually against hundreds of checkpoints. AI extracts and structures relevant information from specifications, visualizing compliance results. Reviewers can efficiently perform final verification.
* **Technical Manual Quality Verification**
   * Verify that complex technical manuals comply with internal guidelines and industry standards. Support the process of comparing tens of thousands of pages of technical documentation annually against thousands of quality criteria. Automatically detect missing technical information and inconsistencies, supporting the creation of consistent, high-quality manuals.
* **Procurement Document Compliance Verification**
   * Check that procurement documents and proposals meet necessary requirements. Automatically extract required information from documents spanning hundreds of pages, streamlining thousands of document reviews annually. Improve procurement process speed and accuracy by having humans verify compliance results against requirement lists.

## Deploy to AWS

You can deploy using the button below. Please click after logging into AWS.

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">Tokyo</option>
      <option value="us-west-2">Oregon</option>
      <option value="us-east-1">Virginia</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=RapidDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/RapidDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### Parameter Settings

You can configure the following parameters during deployment:

* **NotificationEmailAddress**: Email address to receive deployment notifications
* **AllowedIpV4AddressRanges**: IPv4 address ranges allowed for access (JSON array format)
* **AllowedIpV6AddressRanges**: IPv6 address ranges allowed for access (JSON array format)
* **DisableIpv6**: Whether to disable IPv6 support (default: false)
* **AutoMigrate**: Whether to automatically run database migration during deployment (default: true)
* **CognitoSelfSignUpEnabled**: Whether to enable self-signup functionality for Cognito User Pool (default: true)
* **CognitoUserPoolId**: Existing Cognito User Pool ID (creates new if empty)
* **CognitoUserPoolClientId**: Existing Cognito User Pool Client ID (creates new if empty)
* **CognitoDomainPrefix**: Cognito domain prefix (auto-generated if empty)
* **McpAdmin**: Whether to grant administrator privileges to MCP runtime Lambda function (default: false)
* **RepoUrl**: Repository URL to deploy
* **Branch**: Branch name to deploy (default: main)
* **GitTag**: Git tag name to deploy (takes priority over branch if specified)

!!! warning "Security Considerations"
    For production use, the following security measures are recommended:

    1. **IP Restrictions**: Use `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` to restrict access to specific IP addresses
    2. **Disable Self-Signup**: Set `CognitoSelfSignUpEnabled` to `false` and have administrators create users
    3. **Proper Access Control**: Implement appropriate access controls when handling sensitive documents

### Post-Deployment Setup

After clicking the deployment button, you will receive an email titled `AWS Notification - Subscription Confirmation`. Click the `Confirm subscription` link to start receiving deployment start and completion notifications.

When deployment is complete, you'll receive a notification email containing:

1. **Frontend URL**: URL to access the application
2. **API URL**: API endpoint URL
3. **Amazon Bedrock Model Access Setup**: Instructions for enabling access to required models
   - Anthropic Claude 3.7 Sonnet
   - Amazon Nova Premier
4. **User Creation Instructions**: How to create users when self-signup is disabled
5. **Configuration Information**: Confirmation of parameters specified during deployment

### Try RAPID

After deployment is complete, you can try RAPID using the following sample files.

#### Download Sample Files

RAPID requires two types of files: checklist files and review document files. You can download English sample files from the links below:

| Use Case | Checklist | Review Document |
|----------|-----------|----------------|
| **Use Case 001: House Maker Meeting Minutes** | [Meeting Minutes Checklist](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation/blob/main/examples/en/use_case_001_house_maker_meeting_minutes/check_list_meeting_minutes.pdf) | [Floor Plan](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation/blob/main/examples/en/use_case_001_house_maker_meeting_minutes/review_document_floor_plan.png) |
| **Use Case 004: Internal Approval Request (IT Department)** | [Internal Approval Checklist](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation/blob/main/examples/en/use_case_004_internal_approval_request/check_list_internal_approval.pdf) | [Internal Approval Request](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation/blob/main/examples/en/use_case_004_internal_approval_request/review_document_internal_approval_request.pdf) |

For additional sample files and detailed usage instructions, please refer to [RAPID Examples](https://github.com/aws-samples/review-and-assessment-powered-by-intelligent-documentation/tree/main/examples).

### Resource Removal

To remove deployed resources, delete the `RapidStack` and `RapidDeploymentStack` stacks from the CloudFormation console.

## How to Use

1. **Create Checklists**: Create and upload checklists to be used for reviews
2. **Upload Documents**: Upload documents to be reviewed to the system
3. **Execute AI Review**: System automatically analyzes documents and compares them against checklists
4. **Review and Modify Results**: Humans review AI results and make corrections as needed
5. **Final Approval**: Finalize review results and generate reports
