# AWS Generative AI Asset Box

本リポジトリは、[AWS CDK](https://aws.amazon.com/jp/cdk/) で開発されたアセットを 1click / 1command でデプロイするための手順とツールを提供します。アセットとしては、[Generative AI Use Cases JP](https://github.com/aws-samples/generative-ai-use-cases-jp) や [Bedrock Claude Chat](https://github.com/aws-samples/bedrock-claude-chat) 、また 3rd Party の [Dify](https://github.com/aws-samples/dify-self-hosted-on-aws) 等を扱います。

実装として、[Bedrock Claude Chat](https://github.com/aws-samples/bedrock-claude-chat) で用意されている `deploy.yaml` を踏襲し CloudFormation で CodeBuild を作成しデプロイ、完了後に Amazon SNS で通知する方式をとります。

## Repository

```
aws-generative-ai-asset-box/
├── build/           # CloudFormation templates and scripts for deployment
│   ├── genu/        
│   ├── bedrock-cc/  # Comming Soon
│   └── dify/        # Comming Soon
├── tests/           # Test for scripts
├── .venv/           # Python virtual environment (created by uv)
├── pyproject.toml   # Python project configuration
└── README.md        # This file
```

### [Generative AI Use Cases JP](https://github.com/aws-samples/generative-ai-use-cases-jp)

 [![](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentProcess&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/genu/GenUDeploymentProcess.yaml) 

Parameters
* Environment (default: dev)
   * `packages/cdk/parameter.ts` で指定する環境です。Environment の値を切り替えることで複数の GenU 環境をデプロイできます
* RAGEnabled (default: false)
   * Knowledge Base での RAG を有効化します
* SelfSignUp (default: false)
   * セルフサインアップの有効 / 無効を切り替えます
* AllowedSignUpEmailDomains
   * カンマ区切りで利用可能なメールドメインを設定します
* AllowedIpV4AddressRanges
   * アクセス可能な IP アドレスを指定 (IPv4)
* AllowedIpV6AddressRanges
   * アクセス可能な IP アドレスを指定 (IPv6)

デフォルトで IP アドレス指定がないため Public Access 可能な状態でデプロイされます。しかし、SelfSignUp が false であるためログインするにはデプロイした AWS アカウントで Cognito を通じアカウントを作成する必要があるようにしています。

### [Bedrock Claude Chat](https://github.com/aws-samples/bedrock-claude-chat)

Comming Soon

### [Bedrock Claude Chat](https://github.com/aws-samples/dify-self-hosted-on-aws)

Comming Soon

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
