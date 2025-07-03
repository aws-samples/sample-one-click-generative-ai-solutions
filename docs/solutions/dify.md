# Dify

[Dify](https://dify.ai/jp)は、LLMアプリケーション開発のためのオープンソースプラットフォームです。直感的なGUIを通じて、生成AIを活用したチャットボットやエージェント、複雑なワークフローを簡単に作成できます。Amazon Bedrockなどの様々なLLMと連携し、企業やデベロッパーが独自のAIアプリケーションを迅速に構築・展開することを可能にします。

## 主な特徴

- **直感的なGUIインターフェース**: コーディング不要でAIアプリケーションを構築
- **複数LLMサポート**: Amazon Bedrockを含む様々なLLMとの連携
- **RAG（検索拡張生成）**: ナレッジベースを活用した精度の高い回答生成
- **APIとプラグイン**: 既存システムとの連携や機能拡張が容易
- **マルチステップワークフロー**: 複雑なAIワークフローの視覚的な構築
- **セルフホスティング**: AWSマネージドサービスを活用した安全な環境構築

## Parameters

* NotificationEmailAddress
    * Email address for receiving notifications about deployment start and completion.
* Region
    * The region where the deployment will occur.
* AutoPause
    * Toggles automatic database pausing ON/OFF. Recovery after automatic pause takes approximately 10 seconds.
* AllowedIpV4Ciders
    * Allowed IPv4 CIDR ranges for connections (e.g., 0.0.0.0/1).
* AllowedIpV6Ciders
    * Allowed IPv6 CIDR ranges for connections (e.g., ::/1).
