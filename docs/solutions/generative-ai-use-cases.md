# Generative AI Use Cases

[Generative AI Use Cases](https://github.com/aws-samples/generative-ai-use-cases-jp) は、生成 AI の様々なユースケースがあらかじめ組み込まれたアプリケーションです。生成 AI の活用をこれから社内に普及するにあたり、安全かつ誰もが容易に使える環境を構築したい場合に最適です。

## 主な機能

- **多様なユースケース**: チャット、要約、翻訳、画像生成など鉄板の生成 AI ユースケースを体験できます
- **RAG機能**: 各種ドキュメントを参照した検索・生成を行う RAG 機能を利用できます
- **セキュアな環境**: IP 制限や認証など、企業内での安全な利用のためのセキュリティ機能が実装済みです
- **マルチモデル対応**: Amazon Bedrock の様々なモデルを利用できます
- **カスタマイズ可能**: ユースケースビルダーを用い、独自のユースケースを追加・共有できます

## 組織での活用シナリオ

- [オウンドメディア記事作成の効率化 : サルソニード様事例](https://aws.amazon.com/jp/blogs/news/genai-case-study-salsonido/)
- [衣服デザイン等に活用し月 450 時間以上の工数を削減。デジタル人材育成を推進 : タキヒヨー様](https://aws.amazon.com/jp/solutions/case-studies/takihyo/)
- [メルマガ作成・校正ツールを開発し月 200 時間の工数削減を実現 : オイシックス・ラ・大地様](https://aws.amazon.com/jp/solutions/case-studies/oisix/)
    - [AWS Summit 2025 でのご講演](https://youtu.be/rd8PIxrOjHw?si=wBj7wUZJXTd9CEOG)
- [カメラ付き照明による冠水検知にむけた素早い実証実験 : 岩崎電機様](https://aws.amazon.com/jp/blogs/news/genai-case-study-iwasaki/)

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
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-rocket"></i>　Deploy
    </a>
    <a href="https://ap-northeast-1.console.aws.amazon.com/cloudformation/home#/stacks/create/review?stackName=GenUDeploymentStack&amp;param_UsePreviousDeploymentParameter=true&amp;templateURL=https://aws-ml-jp.s3.ap-northeast-1.amazonaws.com/asset-deployments/GenUDeploymentStack.yaml" class="deployment-button md-button" target="_blank">
      <i class="fa-solid fa-sync"></i>　Update
    </a>
  </div>
  <div class="deployment-help">
    <strong>初回デプロイ:</strong> Deploy ボタンを使用してください。<br>
    <strong>デプロイ後の更新:</strong> Update ボタンにより Environment、NotificationEmailAddress のみの入力 (他はデフォルト値のままで可) で前回の設定を引き継げます。(<a href="generative-ai-use-cases-update/" target="_blank">詳細な方法を確認</a>)
  </div>
</div>

### パラメーター設定

デプロイする際に、以下のパラメータを設定できます。

* **Environment** (デフォルト: dev)
    * デプロイする環境の種別です。`packages/cdk/parameter.ts` で指定する環境です。Environment の値を切り替えることで複数の GenU 環境をデプロイできます
* **NotificationEmailAddress**
    * デプロイの開始・終了を通知するメールアドレスです
* **ModelRegion**
    * Amazon Bedrock のモデルを提供するリージョンです。GenU で利用するモデルが指定されたリージョンで提供されていない場合、互換性のあるモデルに自動的に変換されます。[対応済みのモデルはこちらから参照できます](https://aws-samples.github.io/generative-ai-use-cases/en/DEPLOY_OPTION.html#change-amazon-bedrock-models)。
* **RAGEnabled** (デフォルト: None)
    * RAG の設定を選択します。"Knowledge-Bases" は Amazon Bedrock Knowledge Bases 、"Kendra" は Amazon Kendra Developer Edition 、"Both" は両方使用します。"Kendra-Enterprise" のように "Enterprise" では Enterprise Edition を使用します
* **AgentCoreEnabled** (デフォルト: true)
    * エージェント機能を有効にします
* **AgentCoreRegion** (デフォルト: us-east-1)
    * エージェントが使用するリージョンです
* **SelfSignUp** (デフォルト: false)
    * セルフサインアップの有効 / 無効を切り替えます
* **AllowedSignUpEmailDomains**
    * カンマ区切りで利用可能なメールドメインを設定します
* **AllowedIpV4AddressRanges**
    * アクセス可能な IP アドレスを指定 (IPv4)
* **AllowedIpV6AddressRanges**
    * アクセス可能な IP アドレスを指定 (IPv6)

!!! warning "セキュリティに関する注意点"
    
    本番環境で使用する場合は、以下のセキュリティ対策を推奨します：
    
    1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
    2. **セルフサインアップの無効化**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成
    3. **メールドメイン制限**: `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可
    
    IP 制限を設定しない場合は Public Access 可能な状態でデプロイされますが、SelfSignUp は false にしているためログインには AWS アカウントでのユーザー作成 (Amazon Cognito) が必要です。

!!! tip "Experimental : GenU で使える AgentCore エージェントを設定する"

    ワンクリックデプロイ時に、GenU で使える Agent を自動的に設定します！  
    ご利用いただく場合は **GenU をデプロイ / 更新する前に**、**AgentCoreRegionで指定したリージョンへ**デプロイください。

    | Agent | Description |
    |:------|:------|
    | 👩‍💻 [AWS サポートエージェント](https://aws-samples.github.io/sample-personal-aws-customer-assistant/){:target="_blank"} | AWS を使う際の請求、また GenU の使い方など "よくある質問" にいつでもお答えるするエージェントです |

    技術的には、Integration/GenU のタグがつけられた Stack を検索し、見つかった場合 GenU デプロイパラメーターの一つである `agentCoreExternalRuntimes` に Stack で出力されている "AgentCoreRuntimeArn" を `arn` 、 "AgentCoreRuntimeName" を `name` / `description` として登録します。  
    タグ / Stack の Outputs をこの設定で行いデプロイしておけば、**自作のエージェントを簡単に GenU で使うことができます**。



### デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. アプリケーションのURL
2. 管理者アカウントの作成方法
3. Amazon Bedrockのモデルアクセス設定手順

### リソースの削除

デプロイしたリソースを削除するには、CloudFormationコンソールから `GenerativeAiUseCasesStack` と `GenUDeploymentStack` スタックを削除します。

## デプロイ後の活用方法

Generative AI Use Cases の使い方を学ぶには、以下のワークショップを参照してください。

* [生成 AI 体験ワークショップ](https://catalog.workshops.aws/generative-ai-use-cases-jp)


## 関連ドキュメント

- [アップデート手順](generative-ai-use-cases-update.md) - 既存環境のアップデート方法

