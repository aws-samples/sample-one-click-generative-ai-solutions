# Generative AI Use Cases

## Parameters

* Environment (default: dev)
    * This is the type of environment to deploy. It's the environment specified in `packages/cdk/parameter.ts`. By switching the Environment value, you can deploy multiple GenU environments.
* NotificationEmailAddress
    * Email address for receiving notifications about deployment start and completion.
* ModelRegion
    * The region where Amazon Bedrock models will be used.
* RAGEnabled (default: false)
    * Enables RAG (Retrieval-Augmented Generation) for Knowledge Base.
* SelfSignUp (default: false)
    * Toggles self-signup functionality on/off.
* AllowedSignUpEmailDomains
    * Sets permitted email domains separated by commas.
* AllowedIpV4AddressRanges
    * Specifies accessible IP addresses (IPv4).
* AllowedIpV6AddressRanges
    * Specifies accessible IP addresses (IPv6).

It is recommended to set IP restrictions using `AllowedIpV4AddressRanges` and `AllowedIpV6AddressRanges` whenever possible. If IP restrictions are not set, the deployment will be publicly accessible, but since SelfSignUp is set to false by default, login requires user creation in the AWS account (via Amazon Cognito).
