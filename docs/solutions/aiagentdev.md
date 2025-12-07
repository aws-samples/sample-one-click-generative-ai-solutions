# AI Agent Development Code Server

AI Agent Development Code Server は、Amazon Bedrock Agent Core を活用した AI エージェントの開発に必要なソフトウェア等が事前セットアップされた開発環境です。ブラウザベースの VS Code ([Code-Server](https://github.com/coder/code-server)) を使用し、AWS 上に開発環境を構築します。

## 主な機能

- **ブラウザベース開発環境** - code-server による VS Code 互換の開発体験
- **事前設定済み開発ツール** - AWS CLI、SAM CLI、Kiro CLI、uv、Docker などを標準装備
- **Amazon Bedrock Agent Core 対応** - エージェント開発に必要な権限とツールを事前設定
- **CloudFront 経由のセキュアアクセス** - HTTPS による安全な接続
- **自動環境構築** - SSM Document による一貫性のある環境セットアップ

活用いただいた記事

* [ワンクリックでKiro-CLI環境を構築できる「AI Agent Development Code Server」を試してみた](https://dev.classmethod.jp/articles/kiro-ai-agent-development-code-server/)

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="ap-northeast-1">東京</option>
      <option value="ap-northeast-3">大阪</option>
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
    </select>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=AIAgentDevDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/AIAgentDevelopmentCodeServerDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>


### パラメーター設定

デプロイ時に以下のパラメーターを設定できます：

- **UserEmail** (必須)
    - ユーザーのメールアドレスです。Git 設定と Code Server のユーザー名として使用されます。
    - デプロイ完了通知もこのアドレスに送信されます。
- **UserFullName** (デフォルト: AIAgent Developer)
    - Git 設定に使用されるフルネームです。
- **InstanceType** (デフォルト: t4g.medium)
    - EC2 インスタンスタイプです。ARM64 アーキテクチャ (Graviton) のインスタンスを使用します。性能、価格は以下を目安にしてください。特に価格は[最新の情報](https://aws.amazon.com/jp/ec2/pricing/on-demand/)を確認することを推奨します。ハイパフォーマンスな環境が必要な場合、m7g/c7g を検討ください。
    - t4g.small : 2 vCPU + 2G メモリ, 24 時間で 60 円ぐらい
    - t4g.medium : 2 vCPU + 4G メモリ, 24 時間で 120 円ぐらい
    - t4g.large : 2 vCPU + 8G メモリ, 24 時間で 250 円ぐらい
    - t4g.xlarge : 4 vCPU + 16G メモリ, 24 時間で 480 円ぐらい
- **InstanceVolumeSize** (デフォルト: 40)
    - EBS ボリュームサイズ (GB) です。
- **HomeFolder** (デフォルト: /workshop)
    - 作業ディレクトリのパスです。リポジトリがクローンされる場所になります。
- **RepoUrl** (デフォルト: https://github.com/aws-samples/sample-amazon-bedrock-agentcore-onboarding.git)
    - 自動的にクローンする Git リポジトリの URL です。

### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AI Agent Dev Code Server Deployment Notifications - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイが完了したらメールが届くようになります。

デプロイ完了後、通知メールに記載された URL からブラウザベースの開発環境にアクセスし、パスワードを入力し環境にログインしてください。

* パスワードは CloudFormation の出力 / Outputs で確認できます
* 必要に応じ、Amazon Bedrock のモデルを有効化してください
* Kiro CLI が設定済みです。利用する場合、 `kiro-cli login --use-device-flow` を使用し認証を完了してください

### 開発環境の特徴

開発環境には以下のツールが事前インストールされています：

- **AWS ツール**: AWS CLI v2、AWS SAM CLI、Kiro CLI
- **開発ツール**: Git、Docker、Python、UV
- **エディタ**: Code-Server

環境変数も自動設定されます：

- `AWS_REGION` - デプロイしたリージョン
- `AWS_ACCOUNTID` - AWS アカウント ID

### セキュリティ

- EC2 インスタンスへの直接アクセスは制限され、CloudFront 経由のみアクセス可能
- セキュリティグループは CloudFront の Prefix List のみを許可（リージョンごとに設定）
- パスワードは AWS Secrets Manager で安全に管理
- EBS ボリュームは暗号化済み
- SSM Session Manager による管理アクセス

## コスト

主なコストは以下のリソースから発生します：

- **EC2 インスタンス** - t4g.medium (2 vCPU, 4GB メモリ) の実行時間に応じた課金 (t4g.medium、をオンデマンドで 24 時間使った場合 250 円程度です)
- **EBS ボリューム** - 40GB (デフォルト) の gp3 ストレージ料金
- **CloudFront** - データ転送量に応じた課金
- **その他** - VPC、Secrets Manager、SNS などの最小限のコスト

使用しない場合は EC2 インスタンスを停止することでコストを削減できます。ただし、CloudFront と EBS ボリュームは停止中も課金されます。


## リソースの削除

使用を終了する場合は、CloudFormation コンソールからスタックを削除してください：

1. [CloudFormation コンソール](https://console.aws.amazon.com/cloudformation/)にアクセス
2. デプロイしたスタック（デフォルト: `AIAgentDevDeploymentStack`）を選択
3. 「削除」ボタンをクリック

!!! warning "削除時の注意"
    - スタックを削除すると、EC2 インスタンスと EBS ボリュームも削除されます
    - 作業中のコードやデータは事前にバックアップしてください
    - Secrets Manager のシークレットは削除されますが、復旧期間（デフォルト 30 日）があります

## 追加リソース

Amazon Bedrock Agent Core のハンズオンがデフォルトで設定されています。詳細は [README.md](https://github.com/aws-samples/sample-amazon-bedrock-agentcore-onboarding) をご覧ください。

他、書籍のハンズオンを行う際にも活用ください！

* [AIエージェント開発 / 運用入門 [生成AI深掘りガイド]](https://amzn.asia/d/eX6ZBSZ)
* [AWS生成AIアプリ構築実践ガイド](https://amzn.asia/d/cnMEqrO)
