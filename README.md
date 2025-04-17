# AWS Generative AI Asset Box

本リポジトリは、[AWS CDK](https://aws.amazon.com/jp/cdk/) で開発されたアセットを 1click / 1command でデプロイするための手順とツールを提供します。CDK で構築されたアプリケーションを動かすには AWS 環境への接続設定や Node.js のセットアップなど開発者でないと準備が困難でしたが、こちらのリポジトリでは AWS アカウントさえあれば 1 click 、難しい場合でも 1 command でデプロイ・検証できる体験を提供します。

様々なアプリケーションが動かせる AWS のプラットフォームとしての便利さを体感いただければ幸いです。

※本格的な開発やパラメーターのカスタマイズには開発環境が必要なことはご留意ください。

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

1 click の基本的な方式は、CloudFormation で CodeBuild を作成し CDK で構築したアプリケーションをデプロイ、開始 / 完了時に Amazon SNS で通知します。

### [Generative AI Use Cases JP](https://github.com/aws-samples/generative-ai-use-cases-jp)

 [![](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentProcess&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/genu/GenUDeploymentProcess.yaml) 

Parameters
* Environment (default: dev)
   * デプロイする環境の種別です。`packages/cdk/parameter.ts` で指定する環境です。Environment の値を切り替えることで複数の GenU 環境をデプロイできます
* NotificationEmailAddress
   * デプロイの開始・終了を通知するメールアドレスです。
* ModelRegion
   * Amazon Bedrock のモデルを利用するリージョンです
* RAGEnabled (default: false)
   * Knowledge Base での RAG を有効化します
* SelfSignUp (default: false)
   * セルフサインアップの有効 / 無効を切り替えます。
* AllowedSignUpEmailDomains
   * カンマ区切りで利用可能なメールドメインを設定します
* AllowedIpV4AddressRanges
   * アクセス可能な IP アドレスを指定 (IPv4)
* AllowedIpV6AddressRanges
   * アクセス可能な IP アドレスを指定 (IPv6)

できるだけ IP 制限をかけてデプロイすることを推奨します。 IP 制限を書けない場合は Public Access 可能な状態でデプロイされますが、SelfSignUp は false にしているためログインには AWS アカウントでのユーザー作成 (Amazon Cognito) が必要です。


### [Dify](https://github.com/aws-samples/dify-self-hosted-on-aws)

Comming Soon

### [Bedrock Claude Chat](https://github.com/aws-samples/dify-self-hosted-on-aws)

Comming Soon

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
