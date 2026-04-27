# Spec-Driven Presentation Maker (SDPM)

[Spec-Driven Presentation Maker](https://github.com/aws-samples/sample-spec-driven-presentation-maker) は、仕様駆動開発のアプローチでプレゼンテーション資料を作成するオープンソースツールキットです。「何を伝えるか」を先に設計し、「どう見せるか」を AI が構築します。

## 主な機能

- **仕様駆動設計**: ソース資料から論理構造を設計書として定義
- **AI自動構築**: テンプレートに準拠してAIがスライドを自動構築
- **4層アーキテクチャ**: Kiro CLIスキルからフルスタックWebアプリまで
- **MCP対応**: Claude Desktop, VS Code, Kiro等のMCPクライアントで利用可能

![SDPM ワークフロー](./assets/images/solutions/sdpm/workflow-ja.png)

## AWS へのデプロイ

次のボタンからデプロイできます。AWS へログイン後クリックしてください。

<div class="solution-card__actions">
  <div class="solution-card__deployment">
    <select class="region-selector">
      <option value="us-east-1">バージニア</option>
      <option value="us-west-2">オレゴン</option>
      <option value="ap-northeast-1">東京</option>
    </select>
    <a href="https://us-east-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=SdpmDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/SdpmDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
  </div>
</div>

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **DeploymentLayer**: デプロイするレイヤー（デフォルト: layer4）
    - `layer3`: MCPサーバーのみ
    - `layer4`: Agent + Web UIを含むフルスタック
* **SearchSlides**: セマンティックスライド検索の有効化（デフォルト: false）。Bedrock Knowledge Baseを使用します
* **Observability**: Bedrock Model Invocation Loggingの有効化（デフォルト: false）

!!! warning "セキュリティに関する注意点"
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

    1. **IP制限の設定**: アクセス可能なIPアドレスを制限
    2. **セルフサインアップの無効化**: 管理者がユーザーを作成
    3. **メールドメイン制限**: 特定のドメインからのサインアップのみを許可

### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. CloudFront URL
2. Cognitoでのユーザー作成手順

**Layer 4（フルスタック）の場合:**

1. Amazon Cognitoでユーザーを作成
2. CloudFront URLからWebアプリにアクセス

**Layer 3（MCPサーバーのみ）の場合:**

1. MCPクライアント（Claude Desktop, VS Code, Kiro等）からデプロイされたMCPサーバーエンドポイントに接続

### リソースの削除

デプロイしたリソースを削除するには、CloudFormation コンソールから以下のスタックを依存関係の逆順で削除します：

1. `SdpmWebUi`
2. `SdpmAgent`
3. `SdpmRuntime`
4. `SdpmData`
5. `SdpmAuth`
6. `SdpmDeploymentStack`
