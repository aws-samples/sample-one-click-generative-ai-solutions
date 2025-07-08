# Generative AI Use Cases

[Generative AI Use Cases](https://github.com/aws-samples/generative-ai-use-cases-jp) は、生成 AI の様々なユースケースがあらかじめ組み込まれたアプリケーションです。生成 AI の活用をこれから社内に普及するにあたり、安全かつ誰もが容易に使える環境を構築したい場合に最適です。

## 主な機能

- **多様なユースケース**: チャット、要約、翻訳、画像生成など鉄板の生成 AI ユースケースを体験できます
- **RAG機能**: 各種ドキュメントを参照した検索・生成を行う RAG 機能を利用できます
- **セキュアな環境**: IP 制限や認証など、企業内での安全な利用のためのセキュリティ機能が実装済みです
- **マルチモデル対応**: Amazon Bedrock の様々なモデルを利用できます
- **カスタマイズ可能**: ユースケースビルダーを用い、独自のユースケースを追加・共有できます

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **Environment** (デフォルト: dev)
   * デプロイする環境の種別です。`packages/cdk/parameter.ts` で指定する環境です。Environment の値を切り替えることで複数の GenU 環境をデプロイできます
* **NotificationEmailAddress**
   * デプロイの開始・終了を通知するメールアドレスです
* **ModelRegion**
   * Amazon Bedrock のモデルを利用するリージョンです
* **RAGEnabled** (デフォルト: false)
   * Knowledge Base での RAG を有効化します
* **SelfSignUp** (デフォルト: false)
   * セルフサインアップの有効 / 無効を切り替えます
* **AllowedSignUpEmailDomains**
   * カンマ区切りで利用可能なメールドメインを設定します
* **AllowedIpV4AddressRanges**
   * アクセス可能な IP アドレスを指定 (IPv4)
* **AllowedIpV6AddressRanges**
   * アクセス可能な IP アドレスを指定 (IPv6)

## セキュリティに関する注意点

本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
2. **セルフサインアップの無効化**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成
3. **メールドメイン制限**: `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可

IP 制限を設定しない場合は Public Access 可能な状態でデプロイされますが、SelfSignUp は false にしているためログインには AWS アカウントでのユーザー作成 (Amazon Cognito) が必要です。

## デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. アプリケーションのURL
2. 管理者アカウントの作成方法
3. Amazon Bedrockのモデルアクセス設定手順

## 学習リソース

Generative AI Use Cases の使い方を学ぶには、以下のワークショップを参照してください：

* [生成 AI 体験ワークショップ](https://catalog.workshops.aws/generative-ai-use-cases-jp)

## 関連ドキュメント

- [アップデート手順](generative-ai-use-cases-update.md) - 既存環境のアップデート方法

## リソースの削除

デプロイしたリソースを削除するには、CloudFormationコンソールから `GenerativeAiUseCasesStack` と `GenUDeploymentStack` スタックを削除します。
