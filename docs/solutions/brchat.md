# Bedrock Chat

[Bedrock Chat](https://github.com/aws-samples/bedrock-chat) は、Amazon Bedrock を活用した多言語対応の生成 AI プラットフォームです。シンプルなチャット機能だけでなく、ナレッジベース (RAG) を活用したカスタムボット作成、ボットストアを通じたボット共有、エージェント機能によるタスク自動化をサポートしています。生成 AI の特性を理解し、実践的に活用したい場合に最適です。

## 主な機能

- **チャット機能**: Amazon Bedrock の基盤モデルを活用したシンプルなチャットインターフェース
- **カスタムボット作成**: ナレッジベース (RAG) を活用して独自の指示とナレッジを持つボットを作成
- **ボットストア**: 作成したボットをアプリケーションユーザー間で共有
- **エージェント機能**: 複雑なタスクを自動的に処理するエージェント機能
- **API公開**: カスタマイズしたボットをスタンドアロンAPIとして公開可能
- **管理機能**: API管理、ボットの分析、必須ボットの設定など

### パラメータ設定

デプロイ時に以下のパラメータを設定できます：

* **NotificationEmailAddress**: デプロイの開始・終了を通知するメールアドレス
* **BedrockRegion**: Amazon Bedrock のモデルを利用するリージョン（us-east-1, us-west-2, ap-northeast-1）
* **SelfSignUp**: セルフサインアップの有効/無効（デフォルト: false）
* **AllowedSignUpEmailDomains**: サインアップを許可するメールドメイン（カンマ区切り）
* **AllowedIpV4AddressRanges**: アクセスを許可するIPv4アドレス範囲（カンマ区切り）
* **AllowedIpV6AddressRanges**: アクセスを許可するIPv6アドレス範囲（カンマ区切り）
* **EnableRagReplicas**: RAGデータベースのレプリカを有効化（可用性向上、コスト増加）
* **Version**: デプロイするBedrock Chatのバージョン（デフォルト: v3）

## セキュリティに関する注意点

本番環境で使用する場合は、以下のセキュリティ対策を推奨します：

1. **IP制限の設定**: `AllowedIpV4AddressRanges` と `AllowedIpV6AddressRanges` を使用して、アクセス可能なIPアドレスを制限
2. **セルフサインアップの無効化**: `SelfSignUp` を `false` に設定し、管理者がユーザーを作成
3. **メールドメイン制限**: `AllowedSignUpEmailDomains` で特定のドメインからのサインアップのみを許可

## デプロイ後の設定

デプロイのボタンを押すと、しばらくしてから `AWS Notification - Subscription Confirmation` というメールが届くため `Confirm subscription` のリンクを押してください。これで、デプロイの開始、終了のメールが届くようになります。

デプロイが完了すると通知メールが届きます。通知メールには以下の情報が含まれます：

1. フロントエンドURL
2. Amazon Bedrockのモデルアクセス設定手順
3. ユーザー作成手順（セルフサインアップが無効の場合）
4. 特別なグループへのユーザー追加方法：
    - `CreatingBotAllowed`: カスタムボット作成権限
    - `Admin`: 管理者権限
    - `PublishAllowed`: API公開権限

## リソースの削除

デプロイしたリソースを削除するには、CloudFormation コンソールから `BedrockClaudeChat` と `BrChatDeploymentStack` スタックを削除します。
